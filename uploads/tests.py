from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

import io
from PIL import Image

from .models import UploadedFile  # Keep local imports last


class UploadsTestCase(TestCase):
    def setUp(self):
        """Create a test user and log them in."""
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )
        self.client.login(username="testuser", password="password123")

    def create_test_image(self):
        """Generate a valid in-memory image file."""
        image = Image.new("RGB", (100, 100), color="red")
        img_io = io.BytesIO()
        image.save(img_io, format="JPEG")
        img_io.seek(0)
        return SimpleUploadedFile(
            "testimage.jpg",
            img_io.read(),
            content_type="image/jpeg"
        )

    def test_file_upload(self):
        """Test if a user can successfully upload an image."""
        url = reverse("uploads:upload_file")
        test_image = self.create_test_image()

        response = self.client.post(
            url,
            {"name": "Test Image", "file": test_image},
            follow=True
        )

        self.assertEqual(
            response.status_code,
            200,
            "Upload page should load successfully"
        )
        self.assertTrue(
            UploadedFile.objects.filter(
                name="Test Image", user=self.user
            ).exists(),
            "Uploaded file should exist in the database",
        )

    def test_uploaded_files_list(self):
        """Test if uploaded files are listed correctly."""
        UploadedFile.objects.create(
            name="My File",
            file="uploads/testimage.jpg",
            user=self.user
        )

        url = reverse("uploads:uploaded_files")
        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            200,
            "Files list page should load successfully"
        )
        self.assertContains(
            response,
            "My File",
            msg_prefix="Uploaded file should appear in the list"
        )

    def test_file_deletion(self):
        """Test if a user can delete their uploaded file."""
        uploaded_file = UploadedFile.objects.create(
            name="Delete Me",
            file="uploads/delete.jpg",
            user=self.user
        )

        url = reverse("uploads:delete_file", args=[uploaded_file.id])
        response = self.client.post(url, follow=True)

        self.assertEqual(
            response.status_code,
            200,
            "File deletion should redirect successfully"
        )
        self.assertFalse(
            UploadedFile.objects.filter(id=uploaded_file.id).exists(),
            "File should be deleted from the database",
        )

    def test_unauthenticated_access(self):
        """Ensure unauthenticated users are redirected."""
        self.client.logout()

        upload_url = reverse("uploads:upload_file")
        files_url = reverse("uploads:uploaded_files")
        delete_url = reverse("uploads:delete_file", args=[1])

        response_upload = self.client.get(upload_url)
        response_files = self.client.get(files_url)
        response_delete = self.client.post(delete_url)

        self.assertNotEqual(
            response_upload.status_code,
            200,
            "Unauthenticated users should not access upload page",
        )
        self.assertNotEqual(
            response_files.status_code,
            200,
            "Unauthenticated users should not access file list",
        )
        self.assertNotEqual(
            response_delete.status_code,
            200,
            "Unauthenticated users should not delete files",
        )

    def tearDown(self):
        """Clean up test files from the database."""
        UploadedFile.objects.all().delete()
