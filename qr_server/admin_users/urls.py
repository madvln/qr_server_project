from django.urls import path, reverse_lazy
from django.contrib.auth.views import LogoutView

from . import views

app_name = "admin_users"

urlpatterns = [
    path("login/", views.LoginUser.as_view(), name="login"),
    # path("logout/", LogoutView.as_view(), name="logout"),
    path("logout/", views.logout_user, name="logout"),
]
