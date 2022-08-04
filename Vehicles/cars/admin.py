from django.contrib import admin
from .models import Brand,BrandHistory,GeneralClasses#,BrandsClasses,Categories,Car

# Register your models here.
admin.site.register(Brand)
admin.site.register(BrandHistory)
admin.site.register(GeneralClasses)
# admin.site.register(BrandsClasses)
# admin.site.register(Categories)
# admin.site.register(Car)
