from django.contrib import admin
from .models import Product, Category, product_review, product_meta, Tag


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(product_review)
admin.site.register(product_meta)
admin.site.register(Tag)
# Register your models here.
