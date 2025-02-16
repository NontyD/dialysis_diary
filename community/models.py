from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to user
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    class Meta:
        ordering = ['-created_at']  # Newest posts first

    def __str__(self):
        return f"{self.author.username}: {self.content[:50]}"
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"{self.author.username} on {self.post.id}: {self.content[:50]}"
