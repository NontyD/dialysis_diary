from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Event
from django.utils.dateparse import parse_datetime


@login_required
def calendar_view(request):
    """Render calendar template."""
    return render(request, "calendar_app/calendar.html")


@login_required
def event_list(request):
    """Return events in JSON format."""
    events = Event.objects.filter(user=request.user).values("id", "title", "start", "end")
    return JsonResponse(list(events), safe=False)


@csrf_exempt
@login_required
def add_event(request):
    """Add a new event."""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            
            # Validate input fields
            if "title" not in data or "start" not in data:
                return JsonResponse({"error": "Title and start date are required"}, status=400)

            # Convert naive datetime to timezone-aware if necessary
            from django.utils.dateparse import parse_datetime
            from django.utils.timezone import make_aware

            start = parse_datetime(data["start"])
            end = parse_datetime(data.get("end", data["start"]))

            if start is None or end is None:
                return JsonResponse({"error": "Invalid date format"}, status=400)

            # Ensure timezone awareness
            from django.conf import settings
            import pytz
            timezone = pytz.timezone(settings.TIME_ZONE)
            start = make_aware(start, timezone) if start.tzinfo is None else start
            end = make_aware(end, timezone) if end.tzinfo is None else end

            event = Event.objects.create(
                user=request.user,
                title=data["title"],
                start=start,
                end=end
            )
            return JsonResponse({"id": event.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)


@csrf_exempt
@login_required
def update_event(request, event_id):
    """Update event details."""
    event = get_object_or_404(Event, id=event_id, user=request.user)
    if request.method == "POST":
        data = json.loads(request.body)
        event.start = data.get("start", event.start)
        event.end = data.get("end", event.end)
        event.save()
        return JsonResponse({"message": "Event updated"})
    return JsonResponse({"error": "Invalid request"}, status=400)


@csrf_exempt
@login_required
def delete_event(request, event_id):
    """Delete an event."""
    event = get_object_or_404(Event, id=event_id, user=request.user)
    event.delete()
    return JsonResponse({"message": "Event deleted"}, status=204)
