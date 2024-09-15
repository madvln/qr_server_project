from django.contrib import admin
from django.urls import path, include

from admin_panel import urls
from admin_users import urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("admin_panel.urls")),
    path("admin_users/", include("admin_users.urls", namespace="admin_users")),
]
