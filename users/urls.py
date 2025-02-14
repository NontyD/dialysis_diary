from django.urls import path
from .views import register_user, signup_page
from .views import login_page

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('signup/', signup_page, name='signup_page'),
    path("login/", login_page, name="login_page"),
]
