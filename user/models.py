from django.db import models
from django.contrib.auth.models import AbstractUser


class user(AbstractUser):
    mobile = models.CharField(default='', max_length=15)
    passwordHash = models.CharField(default='', max_length=32)
    admin = models.IntegerField
    vendor = models.IntegerField
    registeredAt = models.DateTimeField(auto_now_add=True)
    lastLogin = models.DateTimeField(auto_now=True)
    intro = models.TextField
    profile = models.TextField
