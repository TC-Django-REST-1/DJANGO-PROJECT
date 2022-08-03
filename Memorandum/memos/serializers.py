from rest_framework import serializers
from .models import Category, Task, Comment

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['created_at', 'updated_at']

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ['created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['created_at', 'updated_at']
