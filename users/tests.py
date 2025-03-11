from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib import messages


class UserTests(TestCase):
    def setUp(self):
        """Set up test client, API client, and define URLs."""
        self.client = Client()
        self.api_client = APIClient()

        # Define URLs properly
        self.signup_url = reverse('signup_page')
        self.login_url = reverse('login_page')
        self.settings_url = reverse('account_settings')
        self.delete_url = reverse('delete_account')
        self.dashboard_url = reverse('dashboard')
        self.register_api_url = reverse('register_user')
        self.logout_url = reverse('logout_view')
        self.landing_url = reverse('landing_page')

    def test_signup_page_get(self):
        """Test signup page loads correctly."""
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/signup.html')

    def test_signup_page_post_valid(self):
        """Test successful signup."""
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'testpassword'
        }
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, 302)  # Redirect after signup
        self.assertTrue(User.objects.filter(username='newuser').exists())
        self.assertRedirects(response, self.login_url)

    def test_signup_page_post_invalid(self):
        """Test signup with missing fields."""
        data = {'username': '', 'email': '', 'password': ''}
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, 200)  # Stay on signup page
        self.assertFalse(User.objects.filter(username='').exists())
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(str(messages_list[0]), "All fields are required.")

    def test_signup_page_username_exists(self):
        """Test signup with existing username."""
        User.objects.create_user(
            username='existinguser',
            email='test@example.com',
            password='testpassword'
        )
        data = {
            'username': 'existinguser',
            'email': 'new@example.com',
            'password': 'newpassword'
        }
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, 200)
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(str(messages_list[0]), "Username already taken.")

    def test_signup_page_email_exists(self):
        """Test signup with existing email."""
        User.objects.create_user(
            username='testuser',
            email='existing@example.com',
            password='testpassword'
        )
        data = {
            'username': 'newuser',
            'email': 'existing@example.com',
            'password': 'newpassword'
        }
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, 200)
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(str(messages_list[0]), "Email already registered.")

    def test_login_page_get(self):
        """Test login page loads correctly."""
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_login_page_post_valid(self):
        """Test successful login."""
        User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        data = {'email': 'test@example.com', 'password': 'testpassword'}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.landing_url)

    def test_logout_view(self):
        """Test logout view."""
        User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.login_url)

    def test_account_settings_get(self):
        """Test account settings page loads correctly."""
        User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.settings_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/account_settings.html')

    def test_account_settings_password_change(self):
        """Test changing password."""
        User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='oldpassword'
        )
        self.client.login(username='testuser', password='oldpassword')
        data = {
            'old_password': 'oldpassword',
            'new_password': 'newpassword',
            'confirm_password': 'newpassword'
        }
        response = self.client.post(self.settings_url, data)
        self.assertEqual(response.status_code, 200)

        # Log the user out
        self.client.get(self.logout_url)

        # Try to log in with the new password
        self.assertTrue(
            self.client.login(username='testuser', password='newpassword')
        )

    def test_account_settings_password_mismatch(self):
        """Test password change with mismatched new passwords."""
        User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='oldpassword'
        )
        self.client.login(username='testuser', password='oldpassword')
        data = {
            'old_password': 'oldpassword',
            'new_password': 'newpassword',
            'confirm_password': 'wrongpassword'
        }
        response = self.client.post(self.settings_url, data)
        self.assertEqual(response.status_code, 200)
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(str(messages_list[0]), "New passwords do not match.")

    def test_delete_account_post(self):
        """Test account deletion."""
        User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.login_url)
        self.assertFalse(User.objects.filter(username='testuser').exists())

    def test_dashboard_view(self):
        """Test dashboard view."""
        User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.dashboard_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/dashboard.html')

    def test_register_user_api_valid(self):
        """Test successful user registration via API."""
        data = {
            'username': 'apiuser',
            'email': 'apiuser@example.com',
            'password': 'testpassword'
        }
        response = self.api_client.post(
            self.register_api_url, data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='apiuser').exists())

    def test_register_user_api_email_exists(self):
        """Test user registration API with existing email."""
        User.objects.create_user(
            username='existinguser',
            email='existing@example.com',
            password='testpassword'
        )
        data = {
            'username': 'newuser',
            'email': 'existing@example.com',
            'password': 'newpassword'
        }
        response = self.api_client.post(
            self.register_api_url, data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)
