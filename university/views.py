from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings

from users.serializers import UserAccountSerializer
from .models import Settings, University
from .serializers import UniversitySerializer, UniversitySerializerPublic
from users.permissions import *

from users.models import UserType, UserAccount
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


def change_university_approve_status(request, value):
    university_id = request.data.get('university_id')
    university = University.objects.get(id=university_id)
    previous_approval_status = university.is_approved
    university.is_approved = value
    university.admin.user_type = UserType.ADMIN.value
    university.admin.is_active = value

    if university.admin and university.admin.email:  # Make sure admin and their email exist
        subject = 'University Approval Status Change'
        message = f"Dear {university.admin.get_full_name()},\n\n" \
                  f"The approval status of your university has been changed.\n" \
                  f"Previous Status: {'Approved' if previous_approval_status else 'Not Approved'}\n" \
                  f"New Status: {'Approved' if value else 'Not Approved'}\n\n" \
                  f"Thank you!\n" \
                  f"UniLink Team"

        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [university.admin.email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=True)

    university.save()


@api_view(['POST'])
@permission_classes([UniversityAdminToMod])
def remove_faculty(request):
    faculty_id = request.data.get('faculty_id')
    faculty = UserAccount.objects.get(id=faculty_id)
    faculty.delete()

    return Response({
        'status': 'success',
        'message': 'Faculty deleted'
    })

@api_view(['POST'])
@permission_classes([SiteAdminOnly])
def approve_university(request):
    change_university_approve_status(request, True)

    return Response({
        'status': 'success',
        'message': 'University approved'
    })


@api_view(['POST'])
@permission_classes([SiteAdminOnly])
def disapprove_university(request):
    change_university_approve_status(request, False)

    return Response({
        'status': 'success',
        'message': 'University disapproved'
    })


def change_university_ban_status(request, value):
    university_id = request.data.get('university_id')
    university = University.objects.get(id=university_id)
    university.is_banned = value
    university.save()


@api_view(['POST'])
@permission_classes([SiteAdminOnly])
def ban_university(request):
    change_university_ban_status(request, True)

    return Response({
        'status': 'success',
        'message': 'University banned'
    })


@api_view(['POST'])
@permission_classes([SiteAdminOnly])
def unban_university(request):
    change_university_ban_status(request, False)

    return Response({
        'status': 'success',
        'message': 'University unbanned'
    })


@api_view(['GET'])
@permission_classes([UniversityAdminToMod])
def get_faculty_list(request):
    university = request.user.university
    faculty_list = UserAccount.objects.filter(university=university, user_type=UserType.FACULTY.value)

    return Response(UserAccountSerializer(faculty_list, many=True).data)


@api_view(['POST'])
@permission_classes([UniversityAdminToMod])
def add_faculty(request):
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')
    username = request.data.get('username')
    # generate random password
    password = UserAccount.objects.make_random_password()

    university = request.user.university

    if UserAccount.objects.filter(email=email).exists():
        return Response({
            'status': 'error',
            'message': 'User with this email already exists'
        })

    if UserAccount.objects.filter(username=username).exists():
        return Response({
            'status': 'error',
            'message': 'User with this username already exists'
        })

    user = UserAccount.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        email=email,
        username=username,
        password=password,
        university=university,
        user_type=UserType.FACULTY.value,
        is_active=True
    )

    subject = 'UniLink Account Created'
    message = f"Dear {user.get_full_name()},\n\n" \
                f"Your UniLink account has been created.\n" \
                f"Username: {user.username}\n" \
                f"\nPLease reset passwords to use the account.\n\n" \
                f"Thank you!\n" \
                f"UniLink Team"

    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]

    send_mail(subject, message, from_email, recipient_list, fail_silently=True)

    return Response({
        'status': 'success',
        'message': 'Faculty added'
    })
