from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.validators import MinLengthValidator, MaxLengthValidator
from rest_framework import serializers
from todo.serializers import TodoSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "id")
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        username = validated_data.get("username").lower()
        validate_password(password)
        MinLengthValidator(3, "Minimum username length is 3 character")(username)
        MaxLengthValidator(16, "Maximum username length is 16 character")(username)
        user: User = User.objects.create_user(username=username, password=password)
        user.set_password(password)
        user.save()
        return user

class UserDataSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True)
    class Meta:
        model = User
        fields = ("id", 'username',"todos")