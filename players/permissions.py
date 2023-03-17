from rest_framework import permissions
from .models import Game
from rest_framework.views import Request, View


class IsGameOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Game):
        return request.user.is_authenticated and obj.user.id == request.user.id
