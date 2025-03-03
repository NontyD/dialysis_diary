document.getElementById("togglePostForm").addEventListener("click", function() {
    let form = document.getElementById("postForm");
    if (form.style.display === "none" || form.classList.contains("d-none")) {
        form.classList.remove("d-none");
        form.style.opacity = 0;
        setTimeout(() => { form.style.opacity = 1; form.style.transition = "opacity 0.3s"; }, 10);
    } else {
        form.style.opacity = 0;
        setTimeout(() => { form.classList.add("d-none"); }, 300);
    }
});


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
