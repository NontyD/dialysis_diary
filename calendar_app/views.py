from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event
from .forms import EventForm
from datetime import datetime

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

