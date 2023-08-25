from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from course.models import Course, Section
from users.models import UserAccount
from .serializers import *
from users.permissions import *
from .models import *


@api_view(['GET'])
@permission_classes([AllowAny])
def get_chat_list(request):
    user = request.user
    chat_list = Chat.objects.filter(participants=user)
    serializer = ChatSerializer(chat_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_chat(request):
    user = request.user
    chat_id = request.GET.get('chat_id')
    chat = Chat.objects.get(id=chat_id)

    if chat.university != user.university:
        return Response({
            'status': 'error',
            'message': 'Not Found'
        }, status=404)

    serializer = ChatSerializer(chat)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def create_private_chat(request):
    user = request.user
    participant_id = request.data.get('participant_id')
    participant = UserAccount.objects.get(id=participant_id)

    if participant.university != user.university:
        return Response({
            'status': 'error',
            'message': 'Not Found'
        }, status=404)

    chat = Chat.objects.create(type=ChatType.PRIVATE.value, university=user.university)
    chat.participants.add(user, participant)
    chat.save()

    serializer = ChatSerializer(chat)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def create_classroom_chat(request):
    user = request.user
    section_id = request.data.get('section_id')
    section = Section.objects.get(id=section_id)
    chat = Chat.objects.create(type=ChatType.CLASSROOM.value, university=user.university, section=section)
    chat.participants.add(user)
    chat.save()

    serializer = ChatSerializer(chat)
    return Response(serializer.data)

