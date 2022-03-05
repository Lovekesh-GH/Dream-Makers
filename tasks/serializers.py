
from rest_framework import serializers
from .models import NormalTasks, SpecialTasks



class NormalSerializer(serializers.ModelSerializer):
    """
    Serializer for the comment objects
    """
    class Meta:
        model = NormalTasks
        fields = '__all__'
    

class SpecialSerializer(serializers.ModelSerializer):
    """
    Serializer for the comment objects
    """
    class Meta:
        model = SpecialTasks
        fields = '__all__'
    

