from django.urls import path
from .views import PlayersView, PlayerDetailView, PlayerGameView


urlpatterns = [
    path("players/", PlayersView.as_view()),
    path("players/<int:player_id/", PlayerDetailView.as_view()),
]
