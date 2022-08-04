from rest_framework import serializers

from .models import gather

class gatherSerializer(serializers.ModelSerializer):

    class Meta:
        model= gather
        fields = '__all__'


