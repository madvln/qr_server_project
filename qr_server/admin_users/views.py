from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView

from .forms import LoginAdminUserForm


class LoginUser(LoginView):
    form_class = LoginAdminUserForm
    template_name = "admin_users/login.html"
    extra_context = {"title": "Авторизация"}

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("users:login"))
