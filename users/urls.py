from django.urls import path
from .views import register_user, signup_page
from .views import login_page
from .views import account_settings, delete_account

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('signup/', signup_page, name='signup_page'),
    path("login/", login_page, name="login_page"),
    path("settings/", account_settings, name="account_settings"),
    path("delete/", delete_account, name="delete_account"),
]
