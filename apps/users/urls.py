from apps.users import views
from django.urls import path, include

app_name = "users"

urlpatterns: list[path] = [
    path("", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
]
