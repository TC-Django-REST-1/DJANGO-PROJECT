from django.contrib import admin
from .models import Product,Cafe
# Register your models here.

class CafeAdmin(admin.ModelAdmin):
    list_display=["name","city","open_time","close_time"]

class ProductAdmin(admin.ModelAdmin):
    list_display=["cafe", "name", "description"] 
    list_filter =["name"]

admin.site.register(Product , ProductAdmin)
admin.site.register(Cafe, CafeAdmin)