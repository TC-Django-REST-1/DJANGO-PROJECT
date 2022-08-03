from rest_framework import serializers
from .models import Note, Comment


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class Commenterializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'