console.log("Javascript loaded!");

document.addEventListener("DOMContentLoaded", function () {
    console.log("JavaScript loaded!");

    // Ensure the post form toggle button exists
    let togglePostFormBtn = document.getElementById("togglePostForm");
    let postForm = document.getElementById("postForm");

    if (togglePostFormBtn && postForm) {
        togglePostFormBtn.addEventListener("click", function () {
            postForm.classList.toggle("d-none");
            console.log("Toggled post form.");
        });
    } else {
        console.error("Post button or form not found!");
    }

    // Ensure comment buttons exist
    let commentButtons = document.querySelectorAll(".toggleCommentForm");

    if (commentButtons.length === 0) {
        console.error("No comment buttons found!");
    }

    commentButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            let postItem = button.closest(".list-group-item");
            let commentForm = postItem ? postItem.querySelector(".commentForm") : null;

            if (commentForm) {
                commentForm.classList.toggle("d-none");
                console.log("Toggled comment form.");
            } else {
                console.error("Comment form not found!");
            }
        });
    });
});
