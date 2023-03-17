from django.db import models


class Game(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    is_finish = models.BooleanField(default=False)
    winner = models.CharField(max_length=127, blank=True)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="games"
    )
    players = models.ManyToManyField(
        "players.Player", through="GamePlay", related_name="game"
    )


class GamePlay(models.Model):
    street_points = models.IntegerField(default=0)
    city_points = models.IntegerField(default=0)
    monastery_points = models.IntegerField(default=0)
    farm_points = models.IntegerField(default=0)
    total_score = models.IntegerField(default=0)
    
    player = models.ForeignKey(
        "players.Player", on_delete=models.CASCADE, related_name="gameplay"
    )
    game = models.ForeignKey(
        "games.Game", on_delete=models.CASCADE, related_name="gameplay"
    )
