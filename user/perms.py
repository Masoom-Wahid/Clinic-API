# Permissions
from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser  


class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_staff and not request.user.is_superuser


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff and not request.user.is_superuser


class IsAdminOrStaff(BasePermission):
    SAFE_METHODS = ['GET']
    def has_permission(self, request, view):
        if request.method in self.SAFE_METHODS:
            return True
        return request.user.is_superuser or request.user.is_staff

