from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import *
from users.permissions import *
from rest_framework.response import Response


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
def forum_category_list(request):
    # Get the list of approved forums
    university = request.user.university

    forums = ForumCategory.objects.filter(university=university)
    serializer = ForumCategorySerializer(forums, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AdminToStudent])
def forum_post_list(request):
    forum_id = request.data.get('forum_id')
    forum = Forum.objects.get(id=forum_id)

    # Get the list of approved forums
    forums = ForumPost.objects.filter(forum=forum)
    serializer = ForumPostSerializer(forums, many=True)
    return Response(serializer.data)

