from rest_framework.serializers import ModelSerializer
from .models import Trainer, Course

class TrainerSerializer(ModelSerializer):
    class Meta:
        model = Trainer
        fields = "__all__"

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"