from rest_framework import serializers
from .models import exercise

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = exercise
        fields = '__all__'
