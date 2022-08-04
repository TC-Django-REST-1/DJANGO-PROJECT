from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("id", "title", "body", "done", "created_at", "updated_at")
    
    def create(self, validated_data):
        user: User = self.context.get("request").user
        return Todo.objects.create(author_id=user.pk, **validated_data)
