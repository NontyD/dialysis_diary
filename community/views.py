from django.shortcuts import render, redirect, get_object_or_404
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

@login_required
def edit_post(request, post_id):
    """Allow a user to edit their own post."""
    post = get_object_or_404(Post, id=post_id)

    # Ensure the logged-in user owns the post
    if post.author != request.user:
        messages.error(request, "You can only edit your own posts.")
        return redirect("community")

    if request.method == "POST":
        new_content = request.POST.get("content").strip()

        if not new_content:
            messages.error(request, "Post content cannot be empty.")
        else:
            post.content = new_content
            post.save()
            messages.success(request, "Post updated successfully!")
        return redirect("community")  # Refresh the page

    return render(request, "community/edit_post.html", {"post": post})