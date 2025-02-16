from django.urls import path
from .views import add_record, records_list

urlpatterns = [
    path("", records_list, name="records_home"),
    path("add/", add_record, name="add_record"),
    path("history/", records_list, name="records_list"),
    path("dashboard/", dashboard, name="dashboard"),
]
