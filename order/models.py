from django.db import models
from product.models import Product
from user.models import user


class order(models.Model):
    user = models.ForeignKey(on_delete=models.CASCADE)
    sessionId = models.CharField(default='', max_length=100)
    token = models.CharField(default='', max_length=100)
    status = models.IntegerField(default='', max_length=6)
    subTotal = models.FloatField
    itemDiscount = models.FloatField
    tax = models.FloatField
    shipping = models.FloatField
    total = models.FloatField
    promo = models.CharField(default='', max_length=50)
    discount = models.FloatField
    grandTotal = models.FloatField
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
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    content = models.TextField


class order_item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(order, on_delete=models.CASCADE)
    sku = models.CharField(default='', max_length=100)
    price = models.FloatField
    discount = models.FloatField
    quantity = models.IntegerField(max_length=6)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    content = models.TextField


class transaction(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    order = models.ForeignKey(order, on_delete=models.CASCADE)
    code = models.CharField(default='', max_length=100)
    type = models.IntegerField(max_length=6)
    mode = models.IntegerField(max_length=6)
    status = models.IntegerField(max_length=6)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    content = models.TextField
