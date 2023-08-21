from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import *
from users.permissions import *

from django.db import transaction


@api_view(['POST'])
@permission_classes([AllowAny])
def create_department(request):
    user = request.user
    if not user.is_authenticated:
        return Response({
            'status': 'error',
            'message': 'You are not logged in'
        }, status=401)

    serializer = DepartmentSerializer(data=request.data)
    if serializer.is_valid():
        with transaction.atomic():
            university = serializer.save(university=user.university)  # Assign settings object

            serialized_department = DepartmentSerializer(university)
            return Response(serialized_department.data)

    return Response(serializer.errors, status=400)


@api_view(['GET'])
@permission_classes([SiteAdminOnly])
def department_list(request):
    # Get the list of departments
    departments = Department.objects.filter(university=request.user.university)

    # Serialize the universities
    serializer = DepartmentSerializer(departments, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def department_list_public(request):
    try:
        university = University.objects.get(id=request.data.get('university_id'))
    except University.DoesNotExist:
        return Response({
            'status': 'error',
            'message': 'University not found'
        }, status=404)

    departments = Department.objects.filter(university=university)

    # Serialize the departments
    serializer = DepartmentSerializerPublic(departments, many=True)

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([SiteAdminOnly])
def delete_department(request):
    department_id = request.data.get('department_id')
    try:
        Department.objects.get(id=department_id).delete()
    except Department.DoesNotExist:
        return Response({
            'status': 'error',
            'message': 'Department not found'
        }, status=404)

    return Response({
        'status': 'success',
        'message': 'University approved'
    })

