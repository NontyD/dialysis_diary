from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User


@api_view(['POST'])
def register_user(request):
    """API endpoint to register a user via Django REST Framework."""
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def signup_page(request):
    """Handles user signup through a web form."""
    if request.method == "POST":
        username = request.POST.get("username")  # Required for authentication
        email = request.POST.get("email")
        password = request.POST.get("password")

        print(f"Signup Attempt - Username: {username}, Email: {email}")  # Debugging

        # Validate required fields
        if not username or not email or not password:
            messages.error(request, "All fields are required.")
            return render(request, "users/signup.html")

        # Check if the username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, "users/signup.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, "users/signup.html")

        # Create and save user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        print(f"User {username} successfully registered!")  # Debugging

        messages.success(request, "Account created successfully! Please log in.")
        return redirect("login_page")  # Redirect to login page

    return render(request, "users/signup.html")

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Validation: Check if fields are blank
        if not email or not password:
            messages.error(request, "All fields are required.")
            return render(request, "users/login.html")

        # Fetch the first user matching the email (to prevent multiple object errors)
        user = User.objects.filter(email=email).first()

        if user is None:
            messages.error(request, "Invalid email or password.")
            return render(request, "users/login.html")

        # Authenticate using the username (Django authentication requires username)
        authenticated_user = authenticate(request, username=user.username, password=password)

        if authenticated_user:
            login(request, authenticated_user)
            messages.success(request, "Logged in successfully!")
            return redirect("landing_page")
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, "users/login.html")


@login_required
def account_settings(request):
    """Handles account settings update including name, email, and password."""
    if request.method == "POST":
        user = request.user
        name = request.POST.get("name")
        email = request.POST.get("email")
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        # Update name and email
        if name:
            user.first_name = name
        if email:
            user.email = email

        # Update password only if old password is provided
        if old_password and new_password and confirm_password:
            if not user.check_password(old_password):
                messages.error(request, "Old password is incorrect.")
            elif new_password != confirm_password:
                messages.error(request, "New passwords do not match.")
            else:
                user.set_password(new_password)
                update_session_auth_hash(request, user)  # Keep user logged in
                messages.success(request, "Password updated successfully.")

        user.save()
        messages.success(request, "Account details updated successfully.")

    return render(request, "users/account_settings.html")


@login_required
def delete_account(request):
    """Handles account deletion."""
    if request.method == "POST":
        user = request.user
        user.delete()
        messages.success(request, "Your account has been deleted.")
        return redirect("login_page")  # Redirect to login page after deletion

    return render(request, "users/delete_account.html")
