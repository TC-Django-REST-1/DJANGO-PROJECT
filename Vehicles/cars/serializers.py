from rest_framework import serializers
from .models import Brand,Car


class BrandSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CarSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
