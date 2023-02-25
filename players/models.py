from django.db import models
from games.models import Game


class Player(models.Model):
    username = models.CharField(max_length=55, unique=True)
    street_points = models.IntegerField(default=0)
    history_street_points = models.IntegerField(default=0)
    city_points = models.IntegerField(default=0)
    history_city_points = models.IntegerField(default=0)
    monastery_points = models.IntegerField(default=0)
    history_monastery_points = models.IntegerField(default=0)
    farm_points = models.IntegerField(default=0)
    history_farm_points = models.IntegerField(default=0)
    total_score = models.IntegerField(default=0)
    number_of_wins = models.IntegerField(default=0)
    total_history_score = models.IntegerField(default=0)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="players"
    )
