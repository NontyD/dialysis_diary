from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UploadedFile
from .forms import UploadForm
from django.urls import reverse


@login_required
def upload_file(request):
    """Handle file uploads with a custom name."""
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.user = request.user
            uploaded_file.save()
            messages.success(request, f"File '{uploaded_file.name}' uploaded successfully!")
            return redirect(reverse("uploads:uploaded_files"))
    else:
        form = UploadForm()

    return render(request, "uploads/upload.html", {"form": form})


@login_required
def uploaded_files(request):
    """List uploaded files."""
    files = UploadedFile.objects.filter(user=request.user).order_by("-uploaded_at")
    return render(request, "uploads/files.html", {"files": files})
