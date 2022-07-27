from django.contrib import admin
from .models import Category
from .models import Product
from .models import product_review
from .models import product_meta
from .models import Tag


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(product_review)
admin.site.register(product_meta)
admin.site.register(Tag)
# Register your models here.
