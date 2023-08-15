from rest_framework import serializers
from .models import University
from users.models import UserAccount
from users.serializers import UserAccountSerializer


class UniversitySerializer(serializers.ModelSerializer):
    admin = UserAccountSerializer()

    class Meta:
        model = University
        fields = ['id', 'name', 'domain', 'admin']

    def create(self, validated_data):
        admin_data = validated_data.pop('admin')
        admin = UserAccount.objects.create(**admin_data)
        university = University.objects.create(admin=admin, **validated_data)
        return university


class UniversitySerializerPublic(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'name']
