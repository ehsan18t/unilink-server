import base64
import json

import django.conf
from cryptography.fernet import Fernet
from django.conf import settings
from djoser.social.views import ProviderAuthView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from users.models import UserAccount
from users.permissions import AdminToStudent
from users.serializers import UserAccountSerializer


class CustomProviderAuthView(ProviderAuthView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 201:
            access_token = response.data.get('access')
            refresh_token = response.data.get('refresh')

            response.set_cookie(
                'access',
                access_token,
                max_age=settings.AUTH_COOKIE_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )
            response.set_cookie(
                'refresh',
                refresh_token,
                max_age=settings.AUTH_COOKIE_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )

        return response


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            access_token = response.data.get('access')
            refresh_token = response.data.get('refresh')

            response.set_cookie(
                'access',
                access_token,
                max_age=settings.AUTH_COOKIE_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )
            response.set_cookie(
                'refresh',
                refresh_token,
                max_age=settings.AUTH_COOKIE_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )

        return response


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get('refresh')

        if refresh_token:
            request.data['refresh'] = refresh_token

        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            access_token = response.data.get('access')

            response.set_cookie(
                'access',
                access_token,
                max_age=settings.AUTH_COOKIE_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )

        return response


class CustomTokenVerifyView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        access_token = request.COOKIES.get('access')

        if access_token:
            request.data['token'] = access_token

        return super().post(request, *args, **kwargs)


class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        response = Response(status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie('access')
        response.delete_cookie('refresh')

        return response


@api_view(['GET'])
@permission_classes([AdminToStudent])
def get_user_by_id(request):
    user_id = request.GET.get('user_id')
    user = UserAccount.objects.get(id=user_id)
    serializer = UserAccountSerializer(user, many=False)

    return Response(serializer.data)


def encrypt_json_object(json_object, secret_key):
    # Convert the JSON object to a JSON-formatted string
    json_string = json.dumps(json_object)

    # Create a Fernet cipher with the provided secret key
    cipher = Fernet(secret_key)

    # Encrypt the JSON string
    encrypted_data = cipher.encrypt(json_string.encode())

    return encrypted_data


@api_view(['GET'])
@permission_classes([AdminToStudent])
def get_user_encrypted(request):
    user_id = request.user.id
    user = UserAccount.objects.get(id=user_id)

    if user is None:
        return Response(status=status.HTTP_404_NOT_FOUND)

    print(user)

    serializer = UserAccountSerializer(user, many=False)

    # Ensure the SECRET_KEY is at least 32 bytes long
    secret_key = django.conf.settings.SECRET_KEY[:32]
    # Use base64 encoding to get a 32-byte key
    key = base64.urlsafe_b64encode(secret_key.encode())
    encrypted_data = encrypt_json_object(serializer.data, key)
    print(key)

    return Response({
        'encrypted_data': encrypted_data
    })
