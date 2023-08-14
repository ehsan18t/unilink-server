from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Settings, University
from .serializers import UniversitySerializer, UniversitySerializerPublic
from .permissions import SiteAdminOnly

from django.db import transaction


@api_view(['POST'])
@permission_classes([AllowAny])
def create_university(request):
    serializer = UniversitySerializer(data=request.data)
    if serializer.is_valid():
        with transaction.atomic():
            # Create Settings object
            settings = Settings.objects.create(
                email_pattern='*',
                sid_pattern='*',
                is_registration_enabled=False
            )

            university = serializer.save(settings=settings)  # Assign settings object

            serialized_university = UniversitySerializer(university)
            return Response(serialized_university.data)

    return Response(serializer.errors, status=400)


@api_view(['GET'])
@permission_classes([SiteAdminOnly])
def pending_university_list(request):
    # Get the list of approved universities
    universities = University.objects.filter(is_approved=False)

    # Serialize the universities
    serializer = UniversitySerializer(universities, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([SiteAdminOnly])
def approved_university_list(request):
    # Get the list of approved universities
    universities = University.objects.filter(is_approved=True)

    # Serialize the universities
    serializer = UniversitySerializer(universities, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def approved_university_list_public(request):
    # Get the list of approved universities
    universities = University.objects.filter(is_approved=True)

    # Serialize the universities
    serializer = UniversitySerializerPublic(universities, many=True)

    return Response(serializer.data)
