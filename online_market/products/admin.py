from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'quantity', 'price', 'store']


# Register your models here.
admin.site.register(Product, ProductAdmin)
