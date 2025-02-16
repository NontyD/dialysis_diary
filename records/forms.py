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
        widgets = {
            "average_dwell": forms.TimeInput(format="%H:%M", attrs={"type": "time"}),
            "lost_dwell": forms.TimeInput(format="%H:%M", attrs={"type": "time"}),
            "added_dwell": forms.TimeInput(format="%H:%M", attrs={"type": "time"}),
            "comments": forms.Textarea(attrs={"rows": 3}),
        }
