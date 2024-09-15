# forms.py

from django import forms
from .models import Users

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'slug', 'qr_qode']  # Укажите нужные поля
        # widgets = {
        #     'qr_qode': forms.ClearableFileInput(attrs={'multiple': True}),
        # }