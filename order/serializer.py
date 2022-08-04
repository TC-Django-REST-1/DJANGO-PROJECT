from rest_framework import serializers

from .models import Order

class SerializerOrder(serializers.ModelSerializer):

    class Meta:

        model = Order
        fields = '__all__'

