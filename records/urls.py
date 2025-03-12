from django.urls import path
from .views import add_record, records_list, records_summary

urlpatterns = [
    path("add/", add_record, name="add_record"),
    path("history/", records_list, name="records_list"),
    path("summary/<str:period>/", records_summary, name="records_summary"),
]
