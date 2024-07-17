from django.urls import path
from . import views


app_name = "crm"

urlpatterns: list[path] = [
    path("", views.crm_index, name="crm"),
    path("new-card", views.new_card, name="new_card"),
    # work with 1 card
    path("edit/<int:card_id>", views.edit_card, name="edit_card"),
    path("delete/<int:card_id>", views.delete_card, name="delete_card"),
]
