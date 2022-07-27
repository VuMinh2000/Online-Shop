from django.db import models
from user.models import user


class Category(models.Model):
    title = models.CharField(default='', max_length=75)
    metaTitle = models.CharField(default='', max_length=100)
    slug = models.CharField(default='', max_length=100)
    content = models.TextField(default='')


class Product(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    title = models.CharField(default='', max_length=75)
    mataTitle = models.CharField(default='', max_length=100)
    slug = models.CharField(default='', max_length=100)
    summary = models.TextField(default='')
    Type = models.IntegerField
    sku = models.CharField(default='', max_length=100)
    price = models.FloatField
    discount = models.FloatField
    quantity = models.IntegerField
    shop = models.IntegerField
    createdAt = models.DateTimeField
    updatedAt = models.DateTimeField
    publishedAt = models.DateTimeField
    startAt = models.DateTimeField
    endAt = models.DateTimeField
    content = models.TextField(default='')


class product_review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(default='', max_length=100)
    rating = models.IntegerField
    published = models.IntegerField
    createdAt = models.DateTimeField(auto_now_add=True)
    publishedAt = models.DateTimeField(auto_now=True)
    content = models.TextField


class product_category(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class product_meta(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    key = models.CharField(default='', max_length=50)
    content = models.TextField


class Tag(models.Model):
    title = models.CharField(default='', max_length=75)
    metaTitle = models.CharField(default='', max_length=100)
    slug = models.CharField(default='', max_length=100)
    content = models.TextField(default='')


class product_tag(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
