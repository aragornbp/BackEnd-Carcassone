from .models import Player
from .serializers import PlayerSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .permissions import IsGameOwner


class PlayersView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsGameOwner]
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return Player.objects.filter(user=self.request.user)


class PlayerDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsGameOwner]

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    lookup_url_kwarg = "player_id"
