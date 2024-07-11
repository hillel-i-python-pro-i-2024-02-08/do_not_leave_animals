from django.urls import path
from . import views


app_name = "animals_crm"

urlpatterns: list[path] = [path("", views.crm_index, name="crm_index")]
