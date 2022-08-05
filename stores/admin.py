from django.contrib import admin
from .models import Stores, Products
# Register your models here.

class StoreAdmin(admin.ModelAdmin):
  list_display = ['store_name', 'commercial_registration']

class ProductAdmin(admin.ModelAdmin):
  list_display = ['product_name', 'price', 'stores', 'image_url']

admin.site.register(Stores, StoreAdmin)
admin.site.register(Products, ProductAdmin)