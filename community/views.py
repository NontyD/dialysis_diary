from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post

@login_required
def community_page(request):
    posts = Post.objects.select_related("author").all()  # Fetch posts efficiently
    return render(request, "community/community.html", {"posts": posts})

@login_required
def community_page(request):
    if request.method == "POST":
        content = request.POST.get("content").strip()

        if not content:
            messages.error(request, "Post cannot be empty.")
        else:
            Post.objects.create(author=request.user, content=content)
            messages.success(request, "Post submitted successfully!")

        return redirect("community")  # Refresh the page

    posts = Post.objects.select_related("author").all()
    return render(request, "community/community.html", {"posts": posts})