document.getElementById("signupForm").addEventListener("submit", async function (e) {
    e.preventDefault(); // Prevent default form submission

    // Get user input
    let username = document.getElementById("username").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let messageElement = document.getElementById("message");

    messageElement.textContent = ""; // Clear previous messages

    // Basic validation
    if (!username || !email || !password) {
        messageElement.textContent = "All fields are required.";
        messageElement.className = "error";
        return;
    }

    // Send data to Django backend
    try {
        let response = await fetch("http://localhost:8000/api/users/register/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ username, email, password })
        });

        let data = await response.json();

        if (response.ok) {
            messageElement.textContent = "User registered successfully!";
            messageElement.className = "success";
            setTimeout(() => window.location.href = "/landing", 2000); // Redirect on success
        } else {
            messageElement.textContent = data.email || data.password || "Signup failed. Try again.";
            messageElement.className = "error";
        }
    } catch (error) {
        messageElement.textContent = "An error occurred. Please try again.";
        messageElement.className = "error";
    }
});
