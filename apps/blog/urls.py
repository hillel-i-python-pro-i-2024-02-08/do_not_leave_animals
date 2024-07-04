from django.urls import path, include
from apps.blog import views

app_name = "blog"

urlpatterns: list[path] = [
    path("", views.index, name="index"),
    path("new_post/", views.index, name="new_post"),
]
