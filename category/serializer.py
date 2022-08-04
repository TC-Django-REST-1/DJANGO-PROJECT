from rest_framework import serializers

from .models import Brand, Product

class SerializerBrand(serializers.ModelSerializer):

    class Meta:

        model = Brand
        fields = '__all__'

class SerializerProduct(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = '__all__'