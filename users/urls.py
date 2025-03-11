from django.urls import path
from .views import (
    register_user, signup_page, login_page,
    account_settings, delete_account, dashboard,
    logout_view
)


urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('signup/', signup_page, name='signup_page'),
    path("login/", login_page, name="login_page"),
    path("settings/", account_settings, name="account_settings"),
    path("delete/", delete_account, name="delete_account"),
    path("dashboard/", dashboard, name="dashboard"),
    path("logout/", logout_view, name="logout_view"),
]
