from django.contrib import admin

# Register your models here.
from .models import Order

class OrderAdmin(admin.ModelAdmin):

    list_display = ['user', 'order', 'quantity', 'created_at']

admin.site.register(Order, OrderAdmin)
