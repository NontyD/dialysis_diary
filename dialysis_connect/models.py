from django.db import models
import cloudinary
import cloudinary.models


class UploadedImage(models.Model):
    image = cloudinary.models.CloudinaryField('image')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id} uploaded at {self.uploaded_at}"
