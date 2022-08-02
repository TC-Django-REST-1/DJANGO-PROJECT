from rest_framework import serializers

from .models import Restaurants, Meals

class RestaurantsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Restaurants
        fields = '__all__'
        


class MealsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Meals
        fields = '__all__'