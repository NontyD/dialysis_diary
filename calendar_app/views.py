from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware
from django.conf import settings
import json
import pytz

from .models import Event


@login_required
def calendar_view(request):
    """Render calendar template."""
    return render(request, "calendar_app/calendar.html")


@login_required
def event_list(request):
    """Return events in JSON format."""
    events = Event.objects.filter(user=request.user).values("id", "title",
                                                            "start", "end")
    return JsonResponse(list(events), safe=False)


@csrf_exempt
@login_required
def add_event(request):
    """Add a new event."""
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request"}, status=400)

    try:
        data = json.loads(request.body)

        if "title" not in data or "start" not in data:
            return JsonResponse({"error": "Title and start date are required"},
                                status=400)

        start = parse_datetime(data["start"])
        end = parse_datetime(data.get("end", data["start"]))

        if start is None or end is None:
            return JsonResponse({"error": "Invalid date format"}, status=400)

        timezone = pytz.timezone(settings.TIME_ZONE)
        start = make_aware(start, timezone) if start.tzinfo is None else start
        end = make_aware(end, timezone) if end.tzinfo is None else end

        event = Event.objects.create(user=request.user, title=data["title"],
                                     start=start, end=end)
        return JsonResponse({"id": event.id}, status=201)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


@csrf_exempt
@login_required
def update_event(request, event_id):
    """Update an existing event."""
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"}, status=405)

    try:
        event = get_object_or_404(Event, id=event_id, user=request.user)
        data = json.loads(request.body)
        event.title = data.get("title", event.title)
        event.save()
        return JsonResponse({"message": "Event updated"}, status=200)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data"}, status=400)


@csrf_exempt
@login_required
def delete_event(request, event_id):
    """Delete an event."""
    event = get_object_or_404(Event, id=event_id, user=request.user)
    event.delete()
    return JsonResponse({"message": "Event deleted"}, status=204)
