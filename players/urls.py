from django.urls import path
from .views import PlayersView, PlayerDetailView


urlpatterns = [
    path("players/", PlayersView.as_view()),
    path("players/<int:player_id/", PlayerDetailView.as_view()),
]
