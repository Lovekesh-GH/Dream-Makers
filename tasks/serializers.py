
from rest_framework import serializers
from .models import NormalTasks, SpecialTasks, Completedtasks, SCompletedtasks



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
    


class CompletedSerializer(serializers.ModelSerializer):
    """
    Serializer for the comment objects
    """
    class Meta:
        model = Completedtasks
        fields = '__all__'
    

class SCompletedSerializer(serializers.ModelSerializer):
    """
    Serializer for the comment objects
    """
    class Meta:
        model = SCompletedtasks
        fields = '__all__'
    



