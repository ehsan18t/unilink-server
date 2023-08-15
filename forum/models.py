from django.db import models
from enum import Enum


class AdminType(Enum):
    ADMIN = 1
    REPRESENTATIVE = 2


class ForumAdmin(models.Model):
    user = models.ForeignKey('users.UserAccount', on_delete=models.CASCADE)
    forum = models.ForeignKey('forum.Forum', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    ADMIN_TYPE_CHOICES = [
        (AdminType.ADMIN.value, 'Admin'),
        (AdminType.REPRESENTATIVE.value, 'Representative'),
    ]

    user_type = models.IntegerField(choices=ADMIN_TYPE_CHOICES, default=AdminType.ADMIN.value)


class ForumCategory(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    university = models.ForeignKey('university.University', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class Forum(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    university = models.ForeignKey('university.University', on_delete=models.CASCADE)
    category = models.ForeignKey('forum.ForumCategory', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class ForumPost(models.Model):
    author = models.ForeignKey('users.UserAccount', on_delete=models.CASCADE)
    forum = models.ForeignKey('forum.Forum', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class ForumPostComment(models.Model):
    author = models.ForeignKey('users.UserAccount', on_delete=models.CASCADE)
    forum_post = models.ForeignKey('forum.ForumPost', on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class ForumPostLike(models.Model):
    user = models.ForeignKey('users.UserAccount', on_delete=models.CASCADE)
    forum_post = models.ForeignKey('forum.ForumPost', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
