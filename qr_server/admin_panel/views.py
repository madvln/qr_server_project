from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Users
from .utils import DataMixin
from .forms import UserForm


class AdminPanelHome(DataMixin, ListView):
    template_name = "admin_panel/index.html"
    context_object_name = "users"
    title_page = "Главная страница"

    def get_queryset(self):
        return Users.objects.filter_users(self.request)


class AddUser(DataMixin, CreateView):

    form_class = UserForm
    template_name = "admin_panel/add_user.html"
    title_page = "Добавить Пользователя"

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse("user_info", kwargs={"user_slug": self.object.slug})


class ShowUserInfo(DataMixin, DetailView):
    template_name = "admin_panel/user_info.html"
    slug_url_kwarg = "user_slug"
    context_object_name = "user_info"
    title_page = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_info = context.get("user_info")
        title = user_info.name if user_info else "User Information"
        return self.get_mixin_context(context, title=title)

    def get_object(self, queryset=None):
        return get_object_or_404(
            Users.objects.all(), slug=self.kwargs[self.slug_url_kwarg]
        )
