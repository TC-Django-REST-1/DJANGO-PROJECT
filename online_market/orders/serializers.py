from dataclasses import fields
from datetime import datetime
from rest_framework import serializers
from .models import Order, OrderProduct


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['customer', 'date']

    def set_customer(self, request):
        self.customer = request.user
        self.date = datetime.now()

    def create(self, validated_data):
        validated_data["customer"] = self.customer
        validated_data["date"] = self.date
        return super().create(validated_data)


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = "__all__"
