from rest_framework import serializers
from .models import *


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['first_name', 'last_name', 'username', 'email', 'university', 'department']
