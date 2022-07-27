from django.db import models
from product.models import Product
from user.models import user


class cart(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    sessionId = models.CharField(default='', max_length=100)
    token = models.CharField(default='', max_length=100)
    status = models.IntegerField
    fistName = models.CharField(default='', max_length=50)
    middleName = models.CharField(default='', max_length=50)
    lastName = models.CharField(default='', max_length=50)
    mobile = models.CharField(default='', max_length=15)
    email = models.CharField(default='', max_length=50)
    line1 = models.CharField(default='', max_length=50)
    line2 = models.CharField(default='', max_length=50)
    city = models.CharField(default='', max_length=50)
    province = models.CharField(default='', max_length=50)
    country = models.CharField(default='', max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    content = models.TextField


class cart_item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    sku = models.CharField(default='', max_length=100)
    price = models.FloatField(default='')
    discount = models.FloatField(default='')
    quantity = models.IntegerField
    active = models.IntegerField
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    content = models.TextField(default='')









