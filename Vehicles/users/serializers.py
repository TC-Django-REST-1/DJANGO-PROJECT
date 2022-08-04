from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserEmailSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']
