from rest_framework.serializers import ModelSerializer
from .models import Trainers, Trainees
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']

class TrainerSerializer(ModelSerializer):
    class Meta:
        model = Trainers
        fields = ['start_date','end_date','tr_phone']

class TraineeSerializer(ModelSerializer):
    class Meta:
        model = Trainees
        fields = ['te_phone']