from django.db import models


class user(models.Model):
    fistName = models.CharField(default='', max_length=50)
    middleName = models.CharField(default='', max_length=50)
    lastName = models.CharField(default='', max_length=50)
    mobile = models.CharField(default='', max_length=15)
    email = models.CharField(default='', max_length=50)
    passwordHash = models.CharField(default='', max_length=32)
    admin = models.IntegerField(max_length=1)
    vendor = models.IntegerField(max_length=1)
    registeredAt = models.DateTimeField(auto_now_add=True)
    lastLogin = models.DateTimeField(auto_now=True)
    intro = models.TextField
    profile = models.TextField
