from dataclasses import fields
from rest_framework import serializers
from .models import City, Place

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
