from rest_framework import serializers
from .models import LocalProduct


class LocalProductSerilizer(serializers.ModelSerializer):

    class Meta:
        model = LocalProduct
        fields = '__all__'