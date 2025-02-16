from django.urls import path
from .views import add_event, calendar_view

urlpatterns = [
    path("add/", add_event, name="add_event"),
    path("", calendar_view, name="calendar_view"),
]
