from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer


@api_view(["POST"])
def register_user(request):
    """API endpoint to register a user via Django REST Framework."""
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "User registered successfully"},
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def signup_page(request):
    """Handles user signup through a web form."""
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Clear old messages
        messages.get_messages(request).used = True

        if not username or not email or not password:
            messages.error(request, "All fields are required.")
            return render(request, "users/signup.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, "users/signup.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, "users/signup.html")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return redirect("login_page")

    return render(request, "users/signup.html")


def login_page(request):
    """Handles user login with email authentication."""
    messages.get_messages(request).used = True  # Clear old messages

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password:
            messages.error(request, "All fields are required.")
            return render(request, "users/login.html")

        user = User.objects.filter(email=email).first()

        if user is None:
            messages.error(request, "Invalid email or password.")
            return render(request, "users/login.html")

        authenticated_user = authenticate(request, username=user.username, password=password)

        if authenticated_user:
            login(request, authenticated_user)
            return redirect("landing_page")
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, "users/login.html")


def logout_view(request):
    """Logs out the user and redirects to login."""
    logout(request)
    return redirect("login_page")


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

        if name:
            user.first_name = name
        if email:
            user.email = email

        if old_password and new_password and confirm_password:
            if not user.check_password(old_password):
                messages.error(request, "Old password is incorrect.")
            elif new_password != confirm_password:
                messages.error(request, "New passwords do not match.")
            else:
                user.set_password(new_password)
                update_session_auth_hash(request, user)
                messages.success(request, "Password updated successfully.")

        user.save()

    return render(request, "users/account_settings.html")


@login_required
def delete_account(request):
    """Handles account deletion."""
    if request.method == "POST":
        user = request.user
        user.delete()
        return redirect("login_page")

    return render(request, "users/delete_account.html")


@login_required
def dashboard(request):
    """Dashboard page with quick links to app features."""
    return render(request, "users/dashboard.html")
