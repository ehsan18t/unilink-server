from rest_framework.permissions import BasePermission


class SiteAdminOnly(BasePermission):
    def has_permission(self, request, view):
        # Check if the user has the required type
        return request.user.is_authenticated and request.user.user_type == 0
