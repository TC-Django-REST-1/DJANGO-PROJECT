from rest_framework import serializers

from .models import UserType
from django.contrib.auth.models import User

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = '__all__'