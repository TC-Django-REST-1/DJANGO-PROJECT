from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['store']

    def set_store(self, store):
        self.store = store

    def create(self, validated_data):
        validated_data["store"] = self.store
        return super().create(validated_data)