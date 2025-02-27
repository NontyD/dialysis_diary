from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from cloudinary.models import CloudinaryField


class DialysisRecord(models.Model):
    image = CloudinaryField('image')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to user
    date = models.DateField(default=datetime.today)  # Auto-set current date
    weight_before = models.FloatField(help_text="Weight before dialysis (kg)")
    blood_pressure_systolic = models.IntegerField(help_text="Systolic Blood Pressure")
    blood_pressure_diastolic = models.IntegerField(help_text="Diastolic Blood Pressure")
    initial_drain_volume = models.IntegerField(help_text="Initial Drain Volume (ml)")
    total_uf = models.IntegerField(help_text="Total UF (ml)")
    average_dwell = models.DurationField(help_text="Average Dwell Time (hh:mm)")
    lost_dwell = models.DurationField(help_text="Lost Dwell Time (hh:mm)")
    added_dwell = models.DurationField(help_text="Added Dwell Time (hh:mm)")
    weight_after = models.FloatField(help_text="Weight after dialysis (kg)")
    comments = models.TextField(blank=True, help_text="Additional comments")

    class Meta:
        ordering = ['-date']  # Show most recent records first

    def __str__(self):
        return f"{self.user.username} - {self.date}"