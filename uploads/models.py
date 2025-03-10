from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class UploadedFile(models.Model):
    image = CloudinaryField('image')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  # Custom name field
    file = models.FileField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
