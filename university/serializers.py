from rest_framework import serializers
from .models import University
from users.models import UserAccount


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['first_name', 'last_name', 'username', 'email']


class UniversitySerializer(serializers.ModelSerializer):
    admin = UserAccountSerializer()

    class Meta:
        model = University
        fields = ['name', 'domain', 'admin']

    def create(self, validated_data):
        admin_data = validated_data.pop('admin')
        admin = UserAccount.objects.create(**admin_data)
        university = University.objects.create(admin=admin, **validated_data)
        return university
