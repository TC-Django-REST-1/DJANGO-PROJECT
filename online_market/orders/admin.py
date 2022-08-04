from django.contrib import admin

from .models import Order, OrderProduct


class OrderAdmin(admin.ModelAdmin):
    list_display = ['address', 'date', 'customer']


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity']

# Register your models here.


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
