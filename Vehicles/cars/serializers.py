from rest_framework import serializers
from .models import Brand,BrandHistory,GeneralClasses,Categories#,BrandsClasses,Car


class BrandSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class BrandHistorySerilizer(serializers.ModelSerializer):
    class Meta:
        # model = Brand
        model = BrandHistory
        fields = '__all__'

class GeneralClassesSerilizer(serializers.ModelSerializer):
    class Meta:
        model = GeneralClasses
        fields = '__all__'


# class BrandsClassesSerilizer(serializers.ModelSerializer):
#     class Meta:
#         model = BrandsClasses
#         fields = '__all__'


class CategoriesSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


# class CarSerilizer(serializers.ModelSerializer):
#     class Meta:
#         model = Car
#         fields = '__all__'
