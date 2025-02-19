from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Event
from .forms import EventForm

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
            return redirect("calendar_view")
    else:
        form = EventForm()
    
    return render(request, "calendar_app/add_event.html", {"form": form})


@login_required
def calendar_view(request):
    """Display the user's events."""
    return render(request, "calendar_app/calendar.html")


@login_required
def get_calendar_events(request):
    """Fetch user's events for FullCalendar."""
    events = Event.objects.filter(user=request.user).values("id", "title", "start", "end")
    return JsonResponse(list(events), safe=False)
