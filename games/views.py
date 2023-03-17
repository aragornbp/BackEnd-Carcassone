from .models import Game, GamePlay
from players.models import Player
from .serializers import GameSerializer, GamePlaySerializer
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404
from players.serializers import PlayerSerializer
from rest_framework.exceptions import NotFound


class GameView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return Game.objects.filter(user=self.request.user)


class AddPlayerToGame(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = GamePlay.objects.all()
    serializer_class = GamePlaySerializer

    def get_object(self):
        return super().get_object()

    def perform_create(self, serializer):
        game_selected = get_object_or_404(
            Game,
            id=self.kwargs["game_id"],
            user=self.request.user.id,
        )
        player_selected = get_object_or_404(
            Player,
            id=self.kwargs["player_id"],
            user=self.request.user.id,
        )
        return serializer.save(game=game_selected, player=player_selected)


class ListPlayersInGameView(RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = GameSerializer

    lookup_url_kwarg = "game_id"

    def get_queryset(self):
        game = Game.objects.filter(pk=self.kwargs["game_id"], user=self.request.user.id)
        return game


class RemovePlayerfromGameView(DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    lookup_url_kwarg = "player_id"

    def perform_destroy(self, instance):
        player_obj = get_object_or_404(
            Player,
            pk=self.kwargs["player_id"],
            user=self.request.user.id,
        )

        queryset = get_list_or_404(
            GamePlay,
            game=self.kwargs["game_id"],
            player=player_obj.id,
        )[0]
        return super().perform_destroy(queryset)


class UpdatePlayerInGame(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = GamePlaySerializer

    lookup_url_kwarg = "game_id"

    def get_queryset(self):
        player_obj = get_object_or_404(
            Player,
            pk=self.kwargs["player_id"],
        )

        game_obj = get_object_or_404(
            Game,
            pk=self.kwargs["game_id"],
        )

        gameplay = GamePlay.objects.filter(game=game_obj, player=player_obj)

        return gameplay

    def perform_update(self, serializer):
        player_obj = get_object_or_404(
            Player,
            pk=self.kwargs["player_id"],
        )

        game_obj = get_object_or_404(
            Game,
            pk=self.kwargs["game_id"],
        )
        import ipdb

        ipdb.set_trace()
        return serializer.save(player=player_obj, game=game_obj)
