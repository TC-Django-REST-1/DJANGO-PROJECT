from rest_framework import serializers

from .models import gather, GatherPlayers

class gatherSerializer(serializers.ModelSerializer):

    class Meta:
        model= gather
        fields = '__all__'

class GatherPlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model= GatherPlayers
        fields = '__all__'