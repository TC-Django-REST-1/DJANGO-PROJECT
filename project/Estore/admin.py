from django.contrib import admin
from .models import Product, Category, Company,Comment
# Register your models here.
admin.site.register(Company)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Comment)

admin.site.site_header = "E Shop Review Admin"

