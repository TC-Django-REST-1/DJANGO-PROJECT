from django.contrib import admin
from .models import Brand, Product


class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'established_at_Year')


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'brand', 'type', 'price',
                    'quantity', 'is_active', 'add_at']


admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
