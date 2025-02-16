from django.urls import path
from .views import community_page, edit_post

urlpatterns = [
    path("", community_page, name="community"),
    path("edit/<int:post_id>/", edit_post, name="edit_post"),
]
