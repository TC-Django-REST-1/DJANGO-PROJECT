from rest_framework import serializers
from .models import Product, Cafe


class CafeSerializer(serializers.ModelSerializer):
    class Meta:
        model =Cafe
        fields ='__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =Product
        fields ='__all__'