from rest_framework import serializers

from .models import *


class ForumAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumAdmin
        fields = '__all__'


class ForumCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumCategory
        fields = '__all__'


class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = '__all__'


class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPost
        fields = '__all__'


class ForumPostWithCountSerializer(serializers.ModelSerializer):
    comment_count = serializers.IntegerField()
    upvote_count = serializers.IntegerField()

    class Meta:
        model = ForumPost
        fields = ('id', 'title', 'content', 'author', 'forum', 'created_at', 'updated_at', 'comment_count', 'upvote_count', 'is_active')


class ForumPostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPostComment
        fields = '__all__'


class ForumPostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPostLike
        fields = '__all__'
