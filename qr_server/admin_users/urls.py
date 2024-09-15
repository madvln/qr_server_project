from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = "admin_users"

urlpatterns = [

    path("login/", views.LoginUser.as_view(), name="login"), # "admin_users:login"
    path("logout/", LogoutView.as_view(), name="logout"), # "admin_users:logout"
]
