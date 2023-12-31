from django.db import models
from enum import Enum


class ChatType(Enum):
    CLASSROOM = 1
    PRIVATE = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Chat(models.Model):
    type = models.IntegerField(choices=ChatType.choices())
    created_at = models.DateTimeField(auto_now_add=True)
    participants = models.ManyToManyField('users.UserAccount', related_name='participants')
    section = models.ForeignKey('course.Section', on_delete=models.CASCADE, related_name='chat_section', null=True)
    university = models.ForeignKey('university.University', on_delete=models.CASCADE, related_name='chat_university')

    def __str__(self):
        return f'{self.name}'


class Message(models.Model):
    text = models.CharField(max_length=200)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat')
    user = models.ForeignKey('users.UserAccount', on_delete=models.CASCADE, related_name='user')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text} {self.chat} {self.user}'
