from django.contrib import admin
from .models import Brand,BrandHistory,GeneralClasses,Categories,BrandsClasses,Car


class BrandAdmin(admin.ModelAdmin):
    list_display = [
        'brand',  'established_in', 
        'origin', 'founder', 'headquarters','last_revenue_billion', 
        'year', 
        ]
        # 'description','remarks'
    list_filter = ['brand']


class BrandHistoryAdmin(admin.ModelAdmin):
    list_display = [
        'brand_name',  'established_in', 
        'origin', 'founder', 'headquarters','last_revenue_billion', 
        'year',  'modified_by', 'modification_date'
        ]
        # 'description','remarks'
    list_filter = ['brand_name']


class GeneralClassesAdmin(admin.ModelAdmin):
    list_display = ['general_class', 'remarks']
    list_filter = ['general_class']


class BrandsClassesAdmin(admin.ModelAdmin):
    list_display = [
        'class_name', 'class_brand','general_class', 
        'targeted_customers','quality', 'exclusive',
        ]
        # 'remarks'
    list_filter = ['class_name']


class CategoriesAdmin(admin.ModelAdmin):
    list_display = [
        'category_name', 'targeted_customers','targeted_cost_range',
        'Limited', 
        ]
        # 'remarks'
    list_filter = ['category_name']


class CarAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'car_brand', 'car_class', 'category',
         'price','ongoing_product', 
        ]
        # 'image_url','remarks'
    list_filter = ['name']


# Register your models here.
admin.site.register(Brand, BrandAdmin)
admin.site.register(BrandHistory, BrandHistoryAdmin)
admin.site.register(GeneralClasses, GeneralClassesAdmin)
admin.site.register(BrandsClasses, BrandsClassesAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Car, CarAdmin)
