from django.urls import path
from .views import add_event, calendar_view
from .views import google_calendar_auth, google_calendar_callback

urlpatterns = [
    path("add/", add_event, name="add_event"),
    path("", calendar_view, name="calendar_view"),
    path("oauth/", google_calendar_auth, name="google_calendar_auth"),
    path("oauth/callback/", google_calendar_callback, name="google_calendar_callback"),
]
