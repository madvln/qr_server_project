from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    qr_code = models.ImageField(upload_to='qr_codes/%Y/%m/%d/', blank=True, null=True)
    patronymic = models.CharField(max_length=150, blank=True, null=True)
    is_scanned = models.BooleanField(default=False)