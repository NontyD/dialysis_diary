console.log("Javascript loaded!");

document.addEventListener("DOMContentLoaded", function () {
    // For toggling the post form
    let togglePostFormBtn = document.getElementById("togglePostForm");
    let postForm = document.getElementById("postForm");

    if (togglePostFormBtn && postForm) {
        togglePostFormBtn.addEventListener("click", function () {
            postForm.classList.toggle("d-none");
            console.log("Button clicked! Toggling postForm.");
        });
    } else {
        console.error("Post button or form not found!");
    }

    // For toggling comment forms
    let commentButtons = document.querySelectorAll(".toggleCommentForm");

    commentButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            // Traverse up to the post-item, then find the commentForm within that post
            let postItem = button.closest(".list-group-item");
            let commentForm = postItem.querySelector(".commentForm");

            if (commentForm) {
                commentForm.classList.toggle("d-none");
                console.log("Comment button clicked! Toggling commentForm.");
            } else {
                console.error("Comment form not found!");
            }
        });
    });
});
