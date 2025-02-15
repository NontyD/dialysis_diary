from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.models import User


@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def signup_page(request):
    return render(request, "users/signup.html")


def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Validation: Check if fields are blank
        if not email or not password:
            messages.error(request, "All fields are required.")
            return render(request, "user/login.html")

        # Authenticate user
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("landing_page")  # Redirect to landing page
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, "users/login.html")

@login_required
def account_settings(request):
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
    if request.method == "POST":
        user = request.user
        user.delete()
        messages.success(request, "Your account has been deleted.")
        return redirect("login_page")  # Redirect to login after deletion

    return render(request, "users/delete_account.html")

