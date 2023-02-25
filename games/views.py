from .models import Game
from .serializers import GameSerializer
from rest_framework.generics import (
    ListCreateAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class GameView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user, players=self.request.players)
