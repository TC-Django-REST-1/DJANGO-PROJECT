from rest_framework import serializers
from .models import Store


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        exclude = ['owner']

    def set_owner(self, request):
        self.owner = request.user

    def create(self, validated_data):
        validated_data["owner"] = self.owner
        return super().create(validated_data)
