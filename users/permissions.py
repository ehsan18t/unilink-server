from rest_framework.permissions import BasePermission


class SiteAdminOnly(BasePermission):
    def has_permission(self, request, view):
        # Check if the user has the required type
        return request.user.is_authenticated and request.user.user_type == 0


class UniversityAdminOnly(BasePermission):
    def has_permission(self, request, view):
        # Check if the user has the required type
        return request.user.is_authenticated and request.user.user_type == 1


class FacultyRepresentative(BasePermission):
    def has_permission(self, request, view):
        # Check if the user has the required type
        return request.user.is_authenticated and request.user.user_type == 3 or request.user.user_type == 4


class FacultyToStudent(BasePermission):
    def has_permission(self, request, view):
        # Check if the user has the required type
        return request.user.is_authenticated and request.user.user_type > 2
