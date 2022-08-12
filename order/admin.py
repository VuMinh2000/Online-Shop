from django.contrib import admin
from .models import order, order_item, transaction

admin.site.register(order)
admin.site.register(order_item)
admin.site.register(transaction)

