from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now, timedelta
import json

from .models import Event


class CalendarTestCase(TestCase):
    def setUp(self):
        """Create a test user and log them in."""
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )
        self.client.login(username="testuser", password="password123")

        # Create a test event
        self.event = Event.objects.create(
            user=self.user,
            title="Test Event",
            start=now(),
            end=now() + timedelta(hours=1),
        )

    def test_add_event(self):
        """Test adding a new event via API."""
        url = reverse("add_event")
        event_data = {
            "title": "New Event",
            "start": (now() + timedelta(days=1)).isoformat(),
            "end": (now() + timedelta(days=1, hours=1)).isoformat(),
        }

        response = self.client.post(
            url,
            json.dumps(event_data),
            content_type="application/json",
        )
        self.assertEqual(
            response.status_code, 201, "Event creation should return HTTP 201"
        )
        self.assertTrue(
            Event.objects.filter(title="New Event").exists(),
            "Event should exist in DB",
        )

    def test_event_list(self):
        """Test retrieving a user's events."""
        url = reverse("event_list")
        response = self.client.get(url)

        self.assertEqual(
            response.status_code, 200, "Event list should return HTTP 200"
        )
        self.assertContains(
            response, "Test Event", msg_prefix="Event should appear in list"
        )

    def test_update_event(self):
        """Test updating an existing event."""
        url = reverse("update_event", args=[self.event.id])
        updated_data = {"title": "Updated Event Title"}

        response = self.client.post(
            url,
            json.dumps(updated_data),
            content_type="application/json",
        )

        print("Response Status Code:", response.status_code)
        print("Response Content:", response.content)

        # Reload event from the database
        self.event.refresh_from_db()

        self.assertEqual(
            self.event.title,
            "Updated Event Title",
            "Event title should be updated",
        )

    def test_delete_event(self):
        """Test deleting an event."""
        url = reverse("delete_event", args=[self.event.id])
        response = self.client.post(url)

        self.assertEqual(
            response.status_code, 204, "Event deletion should return HTTP 204"
        )
        self.assertFalse(
            Event.objects.filter(id=self.event.id).exists(),
            "Event should be deleted",
        )

    def test_unauthenticated_access(self):
        """Ensure unauthenticated users are blocked."""
        self.client.logout()

        add_url = reverse("add_event")
        list_url = reverse("event_list")
        update_url = reverse("update_event", args=[self.event.id])
        delete_url = reverse("delete_event", args=[self.event.id])

        self.assertNotEqual(
            self.client.post(add_url).status_code,
            200,
            "Anonymous users cannot add events",
        )
        self.assertNotEqual(
            self.client.get(list_url).status_code,
            200,
            "Anonymous users cannot view events",
        )
        self.assertNotEqual(
            self.client.post(update_url).status_code,
            200,
            "Anonymous users cannot edit events",
        )
        self.assertNotEqual(
            self.client.post(delete_url).status_code,
            200,
            "Anonymous users cannot delete events",
        )

    def tearDown(self):
        """Clean up test events."""
        Event.objects.all().delete()
