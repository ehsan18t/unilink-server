from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Settings
from .serializers import UniversitySerializer

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



