from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post

@login_required
def community_page(request):
    posts = Post.objects.select_related("author").all()  # Fetch posts efficiently
    return render(request, "community/community.html", {"posts": posts})
