from django.urls import path
from .views import *

urlpatterns = [
    path('forum-list/', forum_list, name='forum-list'),
    path('forum-category-list/', forum_category_list, name='forum-category-list'),
    path('forum-post-list/', forum_post_list, name='forum-post-list'),
    path('forum-post-comment-list/', forum_post_comment_list, name='forum-post-comment-list'),
    path('forum-post-like-list/', forum_post_like_list, name='forum-post-like-list'),
]
