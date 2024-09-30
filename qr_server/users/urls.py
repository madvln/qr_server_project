from django.urls import path, register_converter
from . import views

app_name = "users"

urlpatterns = [
    path("", views.index, name="home"),
]