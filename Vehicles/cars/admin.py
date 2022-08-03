from django.contrib import admin
from .models import Brand,Car,BrandHistory,GeneralClasses,BrandsClasses,Categories

# Register your models here.
admin.site.register(Brand)
admin.site.register(Car)
admin.site.register(BrandHistory)
admin.site.register(GeneralClasses)
admin.site.register(BrandsClasses)
admin.site.register(Categories)

