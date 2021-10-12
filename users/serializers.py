from django.contrib.auth.models import User
from django.db.models import fields
from .models import Profile
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username']
class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['user','bio','followers_count','followers']