from django.contrib import admin

from app.models import Product, Rack, Order, OrderItems

# Register your models here.
admin.site.register(Product)
admin.site.register(Rack)
admin.site.register(Order)
admin.site.register(OrderItems)

