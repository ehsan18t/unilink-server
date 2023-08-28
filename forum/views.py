from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from users.permissions import *
from .serializers import *


@api_view(['GET'])
@permission_classes([AdminToStudent])
def forum_list(request):
    # get university id from requested users
    university = request.user.university

    forums = Forum.objects.filter(university=university)
    serializer = ForumSerializer(forums, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AdminToStudent])
def get_forum_by_id(request):
    forum_id = request.GET.get('forum_id')
    forum = Forum.objects.get(id=forum_id)

    serializer = ForumSerializer(forum, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AdminToStudent])
def forum_category_list(request):
    # Get the list of approved forums
    university = request.user.university

    forums = ForumCategory.objects.filter(university=university)
    serializer = ForumCategorySerializer(forums, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AdminToStudent])
def forum_post_list(request):
    forum_id = request.GET.get('forum_id')
    forum = Forum.objects.get(id=forum_id)

    # Get the list of approved forums
    post_list = ForumPost.objects.filter(forum=forum)

    # sort by time (last created on will be first)
    post_list = post_list.order_by('-created_at')

    for post in post_list:
        post.comment_count = ForumPostComment.objects.filter(forum_post=post).count()
        post.upvote_count = ForumPostLike.objects.filter(forum_post=post).count()


    serializer = ForumPostWithCountSerializer(post_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AdminToStudent])
def forum_post_comment_list(request):
    post_id = request.GET.get('post_id')
    post = ForumPost.objects.get(id=post_id)

    # Get the list of approved forums
    comments = ForumPostComment.objects.filter(forum_post=post)
    serializer = ForumPostCommentSerializer(comments, many=True)
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([AdminToStudent])
def get_post_by_id(request):
    post_id = request.GET.get('post_id')
    post = ForumPost.objects.get(id=post_id)

    post.comment_count = ForumPostComment.objects.filter(forum_post=post).count()
    post.upvote_count = ForumPostLike.objects.filter(forum_post=post).count()

    serializer = ForumPostWithCountSerializer(post, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AdminToStudent])
def forum_post_like_list(request):
    post_id = request.data.get('post_id')
    post = ForumPost.objects.get(id=post_id)

    # Get the list of approved forums
    forums = ForumPostLike.objects.filter(post=post)
    serializer = ForumPostLikeSerializer(forums, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([UniversityAdminOnly])
def inactive_forum_forum_list(request):
    university = request.user.university
    forums = Forum.objects.filter(university=university, is_active=False)
    serializer = ForumSerializer(forums, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([UniversityAdminOnly])
def inactive_forum_category_list(request):
    university = request.user.university
    forums = ForumCategory.objects.filter(university=university, is_active=False)
    serializer = ForumCategorySerializer(forums, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AdminToFaculty])
def forum_create(request):
    # get university id from requested users
    university = request.user.university

    # get the forum category id
    category_id = request.data.get('category_id')
    category = ForumCategory.objects.get(id=category_id, is_active=True)

    if category and category.university != university:
        return Response({'error': 'Category does not belong to this university or inactive'})

    # get the forum name
    title = request.data.get('title')

    # get the forum description
    description = request.data.get('description')

    # create the forum
    forum = Forum.objects.create(university=university, category=category, title=title, description=description)

    # add forum admin
    ForumAdmin.objects.create(user=request.user, forum=forum)

    serializer = ForumSerializer(forum, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AdminToStudent])
def forum_post_create(request):
    # get university id from requested users
    university = request.user.university

    # get the forum id
    forum_id = request.data.get('forum_id')
    forum = Forum.objects.get(id=forum_id, is_active=True)

    if university and forum.university != university:
        return Response({'error': 'Forum does not belong to this university or inactive'})

    # get the forum name
    title = request.data.get('title')

    # get the forum description
    content = request.data.get('content')

    # create the forum
    post = ForumPost.objects.create(forum=forum, title=title, content=content, author=request.user)

    serializer = ForumPostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AdminToFaculty])
def forum_category_create(request):
    # get university id from requested users
    university = request.user.university

    # get the forum name
    title = request.data.get('title')

    # get the forum description
    description = request.data.get('description')

    # create the forum
    category = ForumCategory.objects.create(university=university, title=title, description=description)

    serializer = ForumCategorySerializer(category, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AdminToStudent])
def forum_post_comment_create(request):
    # get university id from requested users
    university = request.user.university

    # get the forum id
    post_id = request.data.get('post_id')
    post = ForumPost.objects.get(id=post_id, is_active=True)

    if university and post.forum.university != university:
        return Response({'error': 'Forum does not belong to this university or inactive'})

    # get the forum name
    content = request.data.get('content')

    # create the forum
    comment = ForumPostComment.objects.create(forum_post=post, content=content, author=request.user)

    serializer = ForumPostCommentSerializer(comment, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AdminToStudent])
def toggle_post_vote(request):
    # get university id from requested users
    university = request.user.university

    # get the forum id
    post_id = request.data.get('post_id')
    post = ForumPost.objects.get(id=post_id, is_active=True)

    if university and post.forum.university != university:
        return Response({'error': 'Forum does not belong to this university or inactive'})

    if ForumPostLike.objects.filter(forum_post=post, user=request.user).exists():
        ForumPostLike.objects.filter(forum_post=post, user=request.user).delete()

        return Response(
            {'status': 'success', 'message': 'You have unliked the post'}
        )

    # create the forum
    like = ForumPostLike.objects.create(forum_post=post, user=request.user)

    serializer = ForumPostLikeSerializer(like, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AdminToStudent])
def approve_forum(request):
    forum_id = request.data.get('forum_id')
    forum = Forum.objects.get(id=forum_id)

    forum.is_active = True
    forum.save()

    serializer = ForumSerializer(forum, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AdminToStudent])
def approve_forum_category(request):
    category_id = request.data.get('category_id')
    category = ForumCategory.objects.get(id=category_id)

    if not category or category.university != request.user.university:
        return Response({'error': 'Category does not belong to this university or not found'})

    category.is_active = True
    category.save()

    serializer = ForumCategorySerializer(category, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AdminToStudent])
def get_user_forum_post(request):
    user = request.user
    posts = ForumPost.objects.filter(author=user)
    serializer = ForumPostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AdminToStudent])
def get_posts_for_user(request):
    user = request.user
    all_forum_list = Forum.objects.filter(university=user.university)
    posts = ForumPost.objects.filter(forum__in=all_forum_list)

    # sort by time (last created on will be first)
    posts = posts.order_by('-created_at')

    for post in posts:
        post.comment_count = ForumPostComment.objects.filter(forum_post=post).count()
        post.upvote_count = ForumPostLike.objects.filter(forum_post=post).count()
    serializer = ForumPostWithCountSerializer(posts, many=True)

    return Response(serializer.data)