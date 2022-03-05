from rest_framework.serializers import ModelSerializer
from .models import Users



class UserSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

class UserSerializerforImagefeed(ModelSerializer):
    class Meta:
        model = Users
        fields = ['username']
    
 

class UserSerializerForScoreBoard(ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'profileImage']