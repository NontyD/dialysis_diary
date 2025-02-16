from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event
from .forms import EventForm
from datetime import datetime
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
import os
from django.conf import settings

SCOPES = ["https://www.googleapis.com/auth/calendar.events"]

@login_required
def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            messages.success(request, "Event added successfully!")
            return redirect("calendar_view")
    else:
        form = EventForm()
    return render(request, "calendar_app/add_event.html", {"form": form})

@login_required
def calendar_view(request):
    events = Event.objects.filter(user=request.user).order_by("date")
    return render(request, "calendar_app/calendar.html", {"events": events})

@login_required
def google_calendar_auth(request):
    """Redirect users to Google for authentication."""
    flow = Flow.from_client_secrets_file(
        settings.GOOGLE_CALENDAR_CREDENTIALS,
        scopes=SCOPES,
        redirect_uri=settings.GOOGLE_REDIRECT_URI
    )

    authorization_url, state = flow.authorization_url(
        access_type="offline",
        include_granted_scopes="true"
    )

    request.session["oauth_state"] = state
    return redirect(authorization_url)

@login_required
def google_calendar_callback(request):
    """Handle Google's callback and save user credentials."""
    flow = Flow.from_client_secrets_file(
        settings.GOOGLE_CALENDAR_CREDENTIALS,
        scopes=SCOPES,
        redirect_uri=settings.GOOGLE_REDIRECT_URI
    )

    flow.fetch_token(authorization_response=request.build_absolute_uri())

    credentials = flow.credentials
    request.session["google_credentials"] = {
        "token": credentials.token,
        "refresh_token": credentials.refresh_token,
        "token_uri": credentials.token_uri,
        "client_id": credentials.client_id,
        "client_secret": credentials.client_secret,
        "scopes": credentials.scopes,
    }

    return redirect("calendar_view")  # Redirect to calendar after login