from django.contrib import admin
from .models import order
from .models import order_item
from .models import transaction

admin.site.register(order)
admin.site.register(order_item)
admin.site.register(transaction)

