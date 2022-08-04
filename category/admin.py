from django.contrib import admin

# Register your models here.
from .models import Brand, Product

class BrandAdmin(admin.ModelAdmin):

    list_display = ['name', 'description']

admin.site.register(Brand, BrandAdmin)

class ProductAdmin(admin.ModelAdmin):

    list_display = ['brand', 'name', 'description', 'quantity']

admin.site.register(Product, ProductAdmin)