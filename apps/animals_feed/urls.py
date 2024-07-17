from django.urls import path

from apps.animals_feed import views


app_name = "animals_feed"

urlpatterns: list[path] = [
    path("", views.feed, name="index"),
    path("<int:card_id>/", views.card, name="card"),
]
