from apps.home_page import views
from django.urls import path

app_name = "home_page"

urlpatterns = [
    path("", views.index, name="home"),
]
