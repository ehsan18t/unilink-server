from rest_framework import serializers
from .models import *


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['__all__']

    def create(self, validated_data):
        chat = Chat.objects.create(**validated_data)
        return chat


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['__all__']

    def create(self, validated_data):
        message = Message.objects.create(**validated_data)
        return message
