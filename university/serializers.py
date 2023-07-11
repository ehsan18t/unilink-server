from rest_framework import serializers
from .models import University
from users.models import UserAccount


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['first_name', 'last_name', 'username', 'email', 'profile_picture', 'start_date']


class UniversitySerializer(serializers.ModelSerializer):
    admin = UserAccountSerializer()  # Embed the UserAccount serializer

    class Meta:
        model = University
        fields = ['name', 'domain', 'admin']
