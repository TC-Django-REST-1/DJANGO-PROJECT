from rest_framework import serializers
from django.contrib.auth.models import customers


class customersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = customers
        fields = "__all__"

    def create(self, validated_data):
        customers = super().create(validated_data)
        customers.set_password(validated_data['password'])
        customers.save()
        return customers

    def update(self, instance, validated_data):
        customers = super().update(instance, validated_data)
        try:
            customers.set_password(validated_data['password'])
            customers.save()
        except KeyError:
            pass
        return customers