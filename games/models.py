from django.db import models
from users.models import User


class Game(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    is_finish = models.BooleanField(default=False)
    winner = models.CharField(max_length=127, blank=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="games"
    )
    players = models.ManyToManyField("players.Player", related_name="game")
