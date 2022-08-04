from rest_framework.serializers import ModelSerializer
from .models import Trainers, Trainees
from django.contrib.auth.models import User


class TrainerSerializer(ModelSerializer):
    class Meta:
        model = Trainers
        fields = '__all__'

class TraineeSerializer(ModelSerializer):
    class Meta:
        model = Trainees
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username","email","password"]