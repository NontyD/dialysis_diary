from django.contrib import admin
from .models import UploadedImage  # Make sure this import is correct!


@admin.register(UploadedImage)
class UploadedImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'uploaded_at')
