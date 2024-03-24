from django.contrib import admin

from app.models import Product, Order, OrderItems, ProductPlacement

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(ProductPlacement)
