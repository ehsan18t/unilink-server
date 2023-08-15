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


class ForumPostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPostComment
        fields = '__all__'


class ForumPostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPostLike
        fields = '__all__'
