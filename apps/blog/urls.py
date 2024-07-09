from django.urls import path
from apps.blog import views

app_name = "blog"

urlpatterns: list[path] = [
    path("", views.index, name="index"),
    path("new_post/", views.new_post, name="new_post"),
    path("edit_post/<int:post_id>", views.edit_post, name="edit_post"),
    path("delete_post/<int:post_id>", views.delete_post, name="delete_post"),
    path("post_deleted/", views.post_deleted, name="post_deleted"),
]
