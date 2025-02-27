from django import forms
from .models import UploadedFile


class UploadForm(forms.ModelForm):
    name = forms.CharField(
        max_length=255, required=True, label="File Name",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = UploadedFile
        fields = ["name", "file"]
