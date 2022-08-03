from rest_framework import serializers

from .models import Product, Brand


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ('brand_name', 'established_at_Year')
        depth = 1


class ProductSerializer(serializers.ModelSerializer):
    class Meta:

        model = Product
        fields = '__all__'
        depth = 1
