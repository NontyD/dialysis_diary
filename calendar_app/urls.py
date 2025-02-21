from django.urls import path
from .views import calendar_view, event_list, add_event, update_event, delete_event

urlpatterns = [
    path("", calendar_view, name="calendar_view"),
    path("events/", event_list, name="event_list"),
    path("add_event/", add_event, name="add_event"),
    path("update_event/<int:event_id>/", update_event, name="update_event"),
    path("delete_event/<int:event_id>/", delete_event, name="delete_event"),
]
