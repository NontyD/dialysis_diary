document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("togglePostForm").addEventListener("click", function() {
        document.getElementById("postForm").classList.toggle("d-none");
    });

    document.querySelectorAll(".toggleCommentForm").forEach(button => {
        button.addEventListener("click", function() {
            this.nextElementSibling.classList.toggle("d-none");
        });
    });
});
