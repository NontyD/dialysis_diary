from django.contrib import admin
from .models import DialysisRecord


@admin.register(DialysisRecord)
class DialysisRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'weight_before',
                    'blood_pressure_systolic', 'blood_pressure_diastolic',
                    'initial_drain_volume', 'total_uf', 'average_dwell',
                    'lost_dwell', 'added_dwell', 'weight_after', 'comments')
