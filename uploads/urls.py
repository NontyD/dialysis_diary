from django.urls import path
from .views import upload_file, uploaded_files  

app_name = "uploads"  

urlpatterns = [
    path("upload/", upload_file, name="upload_file"),  
    path("files/", uploaded_files, name="upload_list"),
    path("files/", uploaded_files, name="uploaded_files"),  
]
