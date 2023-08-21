from rest_framework import serializers
from .models import *


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'code', 'university']

    def create(self, validated_data):
        department = Department.objects.create(**validated_data)
        return department


class DepartmentSerializerPublic(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'code']