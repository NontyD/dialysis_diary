from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from .models import Event
from .forms import EventForm
from datetime import datetime
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
import os

# Google Calendar API Scopes
SCOPES = ["https://www.googleapis.com/auth/calendar.events"]

# Use the environment variable for credentials
GOOGLE_CREDENTIALS_PATH = os.getenv("GOOGLE_CREDENTIALS_PATH", "calendar_app/credentials.json")


@login_required
def add_event(request):
    """Allow users to create a new event."""
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            messages.success(request, "Event added successfully!")

            # Sync event to Google Calendar (if linked)
            sync_to_google_calendar(request, event)

            return redirect("calendar_view")
    else:
        form = EventForm()
    
    return render(request, "calendar_app/add_event.html", {"form": form})


@login_required
def calendar_view(request):
    """Display the user's events."""
    events = Event.objects.filter(user=request.user).order_by("date")
    return render(request, "calendar_app/calendar.html", {"events": events})


@login_required
def google_calendar_auth(request):
    """Redirect users to Google for authentication."""
    if request.session.get("google_credentials"):
        messages.info(request, "Your Google Calendar is already linked.")
        return redirect("calendar_view")

    try:
        flow = Flow.from_client_secrets_file(
            GOOGLE_CREDENTIALS_PATH,  # Secure path
            scopes=SCOPES,
            redirect_uri=settings.GOOGLE_REDIRECT_URI
        )

        authorization_url, state = flow.authorization_url(
            access_type="offline",
            include_granted_scopes="true"
        )

        request.session["oauth_state"] = state
        return redirect(authorization_url)

    except Exception as e:
        messages.error(request, f"Google Authentication Failed: {e}")
        return redirect("calendar_view")


@login_required
def google_calendar_callback(request):
    """Handle Google's callback and store user credentials."""
    try:
        flow = Flow.from_client_secrets_file(
            GOOGLE_CREDENTIALS_PATH,  # Secure path
            scopes=SCOPES,
            redirect_uri=settings.GOOGLE_REDIRECT_URI
        )

        flow.fetch_token(authorization_response=request.build_absolute_uri())
        credentials = flow.credentials

        # Store credentials in Django session (temporary for now)
        request.session["google_credentials"] = {
            "token": credentials.token,
            "refresh_token": credentials.refresh_token,
            "token_uri": credentials.token_uri,
            "client_id": credentials.client_id,
            "client_secret": credentials.client_secret,
            "scopes": credentials.scopes,
        }

        messages.success(request, "Google Calendar linked successfully!")
        return redirect("calendar_view")

    except Exception as e:
        messages.error(request, f"Error linking Google Calendar: {e}")
        return redirect("calendar_view")


def sync_to_google_calendar(request, event):
    """Syncs a user's event to Google Calendar if linked."""
    credentials_data = request.session.get("google_credentials")

    if not credentials_data:
        messages.warning(request, "Google Calendar is not linked. Event not synced.")
        return

    try:
        # Recreate credentials from stored session
        credentials = Credentials(**credentials_data)
        service = build("calendar", "v3", credentials=credentials)

        event_data = {
            "summary": event.title,
            "description": event.description,
            "start": {"dateTime": event.date.isoformat(), "timeZone": "UTC"},
            "end": {"dateTime": event.date.isoformat(), "timeZone": "UTC"},
        }

        created_event = service.events().insert(calendarId="primary", body=event_data).execute()

        if created_event:
            messages.success(request, "Event synced to Google Calendar!")

    except Exception as e:
        messages.error(request, f"Failed to sync event: {e}")
