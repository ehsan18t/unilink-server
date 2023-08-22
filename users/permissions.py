from rest_framework.permissions import BasePermission
from .models import UserType


class SiteAdminOnly(BasePermission):
    def has_permission(self, request, view):
        # Check if the user has the required type
        return request.user.is_authenticated and request.user.user_type == UserType.SU.value


class UniversityAdminOnly(BasePermission):
    def has_permission(self, request, view):
        # Check if the user has the required type
        return request.user.is_authenticated and request.user.user_type == UserType.ADMIN.value


class UniversityAdminToMod(BasePermission):
    def has_permission(self, request, view):
        # Check if the user has the required type
        return request.user.is_authenticated and UserType.ADMIN.value >= request.user.user_type <= UserType.MOD.value


class FacultyRepresentative(BasePermission):
    def has_permission(self, request, view):
        # Check if the user has the required type
        return request.user.is_authenticated and request.user.user_type == UserType.FACULTY or request.user.user_type == UserType.REPRESENTATIVE


class FacultyToStudent(BasePermission):
    def has_permission(self, request, view):
        # Check if the user has the required type
        return request.user.is_authenticated and request.user.user_type > UserType.MOD.value


class StudentOnly(BasePermission):
    def has_permission(self, request, view):
        # Check if the user has the required type
        return request.user.is_authenticated and request.user.user_type == UserType.STUDENT.value


class FacultyOnly(BasePermission):
    def has_permission(self, request, view):
        # Check if the user has the required type
        return request.user.is_authenticated and request.user.user_type == UserType.FACULTY.value


class AdminToStudent(BasePermission):
    def has_permission(self, request, view):
        # Check if the user has the required type
        return request.user.is_authenticated and request.user.user_type > -1


class AdminToFaculty(BasePermission):
    def has_permission(self, request, view):
        # Check if the user has the required type
        return request.user.is_authenticated and request.user.user_type < UserType.REPRESENTATIVE.value
