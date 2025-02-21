from rest_framework import serializers
from .models import MoynUser

class MoynUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoynUser
        fields = ['id', 'username', 'profile_url', 'email', 'first_name', 'last_name']