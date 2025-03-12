"""Tests for the records app."""
from datetime import datetime, timedelta

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import DialysisRecord

User = get_user_model()


class DialysisRecordTests(TestCase):
    """Test cases for DialysisRecord model and views."""

    def setUp(self):
        """Set up test user and some dialysis records."""
        self.user = User.objects.create_user(
            username="testuser", password="password"
        )
        self.client.login(username="testuser", password="password")

        self.record1 = DialysisRecord.objects.create(
            user=self.user,
            date=datetime.today().date(),
            weight_before=70,
            blood_pressure_systolic=120,
            blood_pressure_diastolic=80,
            initial_drain_volume=2000,
            total_uf=500,
            average_dwell="04:30",
            lost_dwell="00:30",
            added_dwell="01:00",
            weight_after=69.5,
            comments="Test entry 1"
        )

        self.record2 = DialysisRecord.objects.create(
            user=self.user,
            date=datetime.today().date() - timedelta(days=8),
            weight_before=71,
            blood_pressure_systolic=118,
            blood_pressure_diastolic=78,
            initial_drain_volume=2100,
            total_uf=450,
            average_dwell="04:00",
            lost_dwell="00:20",
            added_dwell="00:40",
            weight_after=69.8,
            comments="Test entry 2"
        )

    def test_add_record_get(self):
        """Test that GET request to add_record renders the form."""
        response = self.client.get(reverse("add_record"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "records/add_record.html")

    def test_add_record_post_no_confirm(self):
        """Test that form submit without confirmation shows confirm page."""
        response = self.client.post(reverse("add_record"), {
            "weight_before": 70,
            "blood_pressure_systolic": 120,
            "blood_pressure_diastolic": 80,
            "initial_drain_volume": 2000,
            "total_uf": 500,
            "average_dwell": "04:30",
            "lost_dwell": "00:30",
            "added_dwell": "01:00",
            "weight_after": 69.5,
            "comments": "Test entry"
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "records/confirm_record.html")

    def test_add_record_post_with_confirm(self):
        """Test that confirming the form submission saves the record."""
        response = self.client.post(reverse("add_record"), {
            "weight_before": 70,
            "blood_pressure_systolic": 120,
            "blood_pressure_diastolic": 80,
            "initial_drain_volume": 2000,
            "total_uf": 500,
            "average_dwell": "04:30",
            "lost_dwell": "00:30",
            "added_dwell": "01:00",
            "weight_after": 69.5,
            "comments": "Test entry",
            "confirm": "true"  # Simulate the confirmation button
        })
        self.assertRedirects(response, reverse("records_list"))
        self.assertTrue(
            DialysisRecord.objects.filter(comments="Test entry").exists()
        )

    def test_records_list(self):
        """Test that records_list displays only logged-in user's records."""
        response = self.client.get(reverse("records_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test entry 1")
        self.assertNotContains(response, "Test entry 2")  # Older than 7 days

    def test_records_summary_week(self):
        """Test that weekly records summary returns correct records."""
        response = self.client.get(reverse("records_summary", args=["week"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test entry 1")
        self.assertNotContains(response, "Test entry 2")

    def test_records_summary_month(self):
        """Test that monthly records summary returns correct records."""
        response = self.client.get(reverse("records_summary", args=["month"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test entry 1")
        self.assertContains(response, "Test entry 2")

    def test_records_summary_invalid_period(self):
        """Test that an invalid period redirects with an error."""
        response = self.client.get(reverse("records_summary", args=["year"]))
        self.assertRedirects(response, reverse("records_list"))
        messages = list(response.wsgi_request._messages)
        self.assertEqual(str(messages[0]), "Invalid period selected.")
