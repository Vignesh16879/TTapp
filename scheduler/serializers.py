from rest_framework import serializers
from .utils import user_login as User
 
 
class userSerializers(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields =  '__all__'