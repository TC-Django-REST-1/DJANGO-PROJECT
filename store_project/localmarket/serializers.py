from rest_framework import serializers
from .models import LocalMarket

class LocalMarketSerilizer(serializers.ModelSerializer):

    class Meta:
        model = LocalMarket
        fields = '__all__'