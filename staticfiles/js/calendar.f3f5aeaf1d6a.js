document.addEventListener("DOMContentLoaded", function () {
    var eventModal = document.getElementById("eventModal");
    var modalOverlay = document.getElementById("modalOverlay");
    var eventTitleEl = document.getElementById("eventTitle");
    var editEventBtn = document.getElementById("editEventBtn");
    var deleteEventBtn = document.getElementById("deleteEventBtn");
    var closeModal = document.getElementById("closeModal");

    var calendarEl = document.getElementById("calendar");
    var selectedEvent = null;

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: "dayGridMonth",
        selectable: true,
        editable: true,
        events: "/calendar/events/",
        headerToolbar: {
            left: "prev,next today",
            center: "title",
            right: "dayGridMonth,timeGridWeek,timeGridDay"
        },
        views: {
            month: {
                displayEventEnd: true,
                eventLimit: true // Prevents overlapping events
            }
        },

        eventRender: function (info) {
            if (window.innerWidth < 768) {
                info.el.querySelector(".fc-title").append(
                    `<br>${moment(info.event.start).format("h:mm A")}`
                );
            }
        },

        select: function (info) {
            var title = prompt("Enter event title:");
            if (!title) return;

            var startDateTime = prompt(
                "Enter start date and time (YYYY-MM-DD HH:MM):",
                info.startStr.replace("T", " ").slice(0, 16)
            );
            if (!startDateTime || !isValidDateTime(startDateTime)) {
                alert("Invalid start time format.");
                return;
            }

            var endDateTime = prompt(
                "Enter end date and time (YYYY-MM-DD HH:MM):",
                info.endStr ? info.endStr.replace("T", " ").slice(0, 16) : startDateTime
            );
            if (!endDateTime || !isValidDateTime(endDateTime)) {
                alert("Invalid end time format.");
                return;
            }

            fetch("/calendar/add_event/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken"),
                },
                body: JSON.stringify({
                    title: title,
                    start: startDateTime,
                    end: endDateTime,
                    allDay: !startDateTime.includes(":") // Fixes "12a" issue
                }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.id) {
                    calendar.refetchEvents();
                } else {
                    alert("Failed to add event: " + data.error);
                }
            })
            .catch(error => console.error("Error:", error));

            calendar.unselect();
        },

        eventClick: function (info) {
            selectedEvent = info.event;
            eventTitleEl.innerText = selectedEvent.title;
            eventModal.style.display = "block";
            modalOverlay.style.display = "block"; // Show overlay to block clicks on the background
        }
    });

    calendar.render();

    // Edit Event
    editEventBtn.onclick = function () {
        if (!selectedEvent) return;

        let newTitle = prompt("Enter new event title:", selectedEvent.title);
        if (!newTitle) return;

        let newStart = prompt(
            "Enter new start time (YYYY-MM-DD HH:MM):",
            selectedEvent.start.toISOString().slice(0, 16).replace("T", " ")
        );
        if (!newStart || !isValidDateTime(newStart)) {
            alert("Invalid start time format.");
            return;
        }

        let newEnd = prompt(
            "Enter new end time (YYYY-MM-DD HH:MM):",
            selectedEvent.end ? selectedEvent.end.toISOString().slice(0, 16).replace("T", " ") : newStart
        );
        if (!newEnd || !isValidDateTime(newEnd)) {
            alert("Invalid end time format.");
            return;
        }

        fetch(`/calendar/update_event/${selectedEvent.id}/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body: JSON.stringify({
                title: newTitle,
                start: newStart,
                end: newEnd
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                selectedEvent.setProp("title", newTitle);
                selectedEvent.setStart(newStart);
                selectedEvent.setEnd(newEnd);
                closeModalFn();
            } else {
                alert("Failed to update event.");
            }
        });
    };

    // Delete Event
    deleteEventBtn.onclick = function () {
        if (!selectedEvent) return;

        if (confirm("Are you sure you want to delete this event?")) {
            fetch(`/calendar/delete_event/${selectedEvent.id}/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken"),
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.message) {
                    selectedEvent.remove();
                    closeModalFn();
                } else {
                    alert("Failed to delete event.");
                }
            })
            .catch(error => console.error("Error:", error));
        }
    };

    // Function to validate date-time input
    function isValidDateTime(dateTimeStr) {
        return /^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$/.test(dateTimeStr);
    }

    // CSRF token function
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            let cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++) {
                let cookie = cookies[i].trim();
                if (cookie.startsWith(name + "=")) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
