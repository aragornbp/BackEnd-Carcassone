from rest_framework import permissions
from rest_framework.views import Request, View
from .models import User


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        return (
            request.user.is_authenticated
            and obj == request.user
            or request.user.is_admin
        )

