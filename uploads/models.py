from django.db import models
from django.contrib.auth.models import User

class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # File belongs to a user
    file = models.FileField(upload_to="uploads/")  # Store in 'uploads/' folder
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp
