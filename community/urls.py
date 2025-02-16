from django.urls import path
from .views import community_page

urlpatterns = [
    path("", community_page, name="community"),
]
