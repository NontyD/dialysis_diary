from django.contrib import admin
from .models import DialysisRecord


@admin.register(DialysisRecord)
class DialysisRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'weight', 'blood_pressure', 'temperature', 'pulse', 'dialysis_time', 'created_at')
