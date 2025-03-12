from django import forms
from .models import DialysisRecord


class DialysisRecordForm(forms.ModelForm):
    class Meta:
        model = DialysisRecord
        fields = [
            "weight_before",
            "blood_pressure_systolic",
            "blood_pressure_diastolic",
            "initial_drain_volume",
            "total_uf",
            "average_dwell",
            "lost_dwell",
            "added_dwell",
            "weight_after",
            "comments"
        ]
        time_input = forms.TimeInput(format="%H:%M", attrs={"type": "time"})
        widgets = {
            "average_dwell": time_input,
            "lost_dwell": time_input,
            "added_dwell": time_input,
            "comments": forms.Textarea(attrs={"rows": 3})
        }
