from rest_framework import serializers
from .models import diet

class DietSerializer(serializers.ModelSerializer):
    class Meta:
        model = diet
        fields = '__all__'
