from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UniversitySerializer


@api_view(['POST'])
def create_university(request):
    serializer = UniversitySerializer(data=request.data)
    if serializer.is_valid():
        university = serializer.save()
        serialized_university = UniversitySerializer(university)
        return Response(serialized_university.data)
    return Response(serializer.errors, status=400)
