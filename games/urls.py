from django.urls import path
from .views import (
    GameView,
    AddPlayerToGame,
    ListPlayersInGameView,
    RemovePlayerfromGameView,
    UpdatePlayerInGame,
)


urlpatterns = [
    path("games/", GameView.as_view()),
    path("games/<int:game_id>/status/", ListPlayersInGameView.as_view()),
    path("games/<int:game_id>/player/<int:player_id>/", AddPlayerToGame.as_view()),
    path(
        "games/<int:game_id>/player/<int:player_id>/remove/",
        RemovePlayerfromGameView.as_view(),
    ),
    path(
        "games/<int:game_id>/player/<int:player_id>/update/teste/",
        UpdatePlayerInGame.as_view(),
    ),
]
