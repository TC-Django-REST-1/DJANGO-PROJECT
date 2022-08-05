from rest_framework import serializers
from .models import Stores, Products

class StoresSerializer(serializers.ModelSerializer):
  class Meta:
    model = Stores
    fields = '__all__'
class ProductsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Products
    fields = '__all__'