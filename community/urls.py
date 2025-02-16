from django.urls import path
from .views import community_page, edit_post, delete_post, add_comment

urlpatterns = [
    path("", community_page, name="community"),
    path("edit/<int:post_id>/", edit_post, name="edit_post"),
    path("delete/<int:post_id>/", delete_post, name="delete_post"),
    path("comment/<int:post_id>/", add_comment, name="add_comment"),
]
