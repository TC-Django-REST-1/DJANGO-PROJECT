from rest_framework import serializers
from .models import Brand#,BrandHistory

#Car,GeneralClasses,BrandsClasses,Categories


class BrandSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


# class CarSerilizer(serializers.ModelSerializer):
#     class Meta:
#         model = Car
#         fields = '__all__'


# class BrandHistorySerilizer(serializers.ModelSerializer):
    # class Meta:
    #     model = BrandHistory
    #     fields = '__all__'


# class GeneralClassesSerilizer(serializers.ModelSerializer):
#     class Meta:
#         model = GeneralClasses
#         fields = '__all__'


# class BrandsClassesSerilizer(serializers.ModelSerializer):
#     class Meta:
#         model = BrandsClasses
#         fields = '__all__'


# class CategoriesSerilizer(serializers.ModelSerializer):
#     class Meta:
#         model = Categories
#         fields = '__all__'
