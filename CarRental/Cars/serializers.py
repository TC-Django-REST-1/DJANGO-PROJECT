from rest_framework import serializers

from .models import Branch
from .models import Car
from .models import reservedCar


# Serialized Branch Model
class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = '__all__'


# Serialized Car Model
class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'


# Serialized reservedCar Model
class reservedCarSerializer(serializers.ModelSerializer):

    class Meta:
        model = reservedCar
        fields = '__all__'