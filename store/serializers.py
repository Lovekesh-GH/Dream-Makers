from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from .models import Store, ProductImage

class storeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'