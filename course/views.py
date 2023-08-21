from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import *
from users.permissions import SiteAdminOnly


@api_view(['GET'])
@permission_classes([AllowAny])
def get_courses(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        return Response(status=404)

    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_section(request):
    section_id = request.GET.get('section_id')

    section = Section.objects.filter(id=section_id)
    serializer = SectionSerializer(section, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_course_sections(request):
    course_id = request.GET.get('course_id')

    course = Course.objects.filter(id=course_id).first()
    sections = Section.objects.filter(course=course)
    return Response(SectionSerializer(sections, many=True).data)
