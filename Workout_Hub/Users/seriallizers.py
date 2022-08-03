from rest_framework.serializers import ModelSerializer
from .models import Trainer, Trainee

class TrainerSerializer(ModelSerializer):
    class Meta:
        model = Trainer
        fields = "__all__"

class TraineeSerializer(ModelSerializer):
    class Meta:
        model = Trainee
        fields = "__all__"