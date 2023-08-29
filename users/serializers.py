from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from department.models import Department
from .models import *
from university.models import University


class CustomUserCreateSerializer(UserCreateSerializer):
    university = serializers.PrimaryKeyRelatedField(queryset=University.objects.all(), required=True)

    class Meta(UserCreateSerializer.Meta):
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'university')


class CustomUserCreateSerializerRetype(CustomUserCreateSerializer):
    class Meta(CustomUserCreateSerializer.Meta):
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'university', 'department')


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'university', 'department', 'profile_picture', 'user_type']
