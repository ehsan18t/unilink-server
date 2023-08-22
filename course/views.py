from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from users.permissions import *
from .serializers import *


@api_view(['GET'])
@permission_classes([AdminToStudent])
def get_courses(request):
    try:
        courses = Course.objects.filter(university=request.user.university)
    except Course.DoesNotExist:
        return Response(status=404)

    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AdminToStudent])
def get_section(request):
    section_id = request.GET.get('section_id')

    section = Section.objects.filter(id=section_id)
    serializer = SectionSerializer(section, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AdminToStudent])
def get_course_sections(request):
    course_id = request.GET.get('course_id')

    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response(status=404)
    print(course)
    sections = Section.objects.filter(course=course)
    return Response(SectionSerializer(sections, many=True).data)


@api_view(['POST'])
@permission_classes([AdminToStudent])
def create_section(request):
    name = request.data.get('name')
    trimester = request.data.get('trimester')
    course_id = request.data.get('course_id')

    try:
        course = Course.objects.filter(id=course_id).first()
    except Course.DoesNotExist:
        return Response(status=404)

    if course is None:
        return Response(status=404)

    section = Section.objects.create(name=name, trimester=trimester, course=course)
    return Response(SectionSerializer(section).data)


@api_view(['POST'])
@permission_classes([AdminToStudent])
def update_section(request):
    section_id = request.data.get('section_id')
    name = request.data.get('name')
    trimester = request.data.get('trimester')

    try:
        section = Section.objects.filter(id=section_id).first()
    except Section.DoesNotExist:
        return Response(status=404)

    if section is None:
        return Response(status=404)

    section.name = name
    section.trimester = trimester
    section.save()
    return Response(SectionSerializer(section).data)


@api_view(['POST'])
@permission_classes([AdminToStudent])
def delete_section(request):
    section_id = request.data.get('section_id')

    try:
        section = Section.objects.filter(id=section_id).first()
    except Section.DoesNotExist:
        return Response(status=404)

    if section is None:
        return Response(status=404)

    section.delete()
    return Response(status=200)
