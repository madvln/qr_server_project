from django.urls import path
from . import views

urlpatterns = [
    path("", views.AdminPanelHome.as_view(), name="home"),
    path("add/", views.AddUser.as_view(), name="add_user"),
    path("user_info/<slug:user_slug>/", views.ShowUserInfo.as_view(), name="user_info"),
]
