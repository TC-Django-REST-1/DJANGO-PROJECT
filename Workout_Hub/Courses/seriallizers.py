from rest_framework.serializers import ModelSerializer
from .models import Trainer, Course

class CoursesSerializer(ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"