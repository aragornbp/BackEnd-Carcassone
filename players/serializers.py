from rest_framework import serializers
from .models import Player, PlayerGame


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = [
            "id",
            "username",
            "street_points",
            "history_street_points",
            "city_points",
            "history_city_points",
            "monastery_points",
            "history_monastery_points",
            "farm_points",
            "history_farm_points",
            "total_score",
            "number_of_wins",
            "total_history_score",
        ]
        read_only_fields = [
            "street_points",
            "history_street_points",
            "city_points",
            "history_city_points",
            "monastery_points",
            "history_monastery_points",
            "farm_points",
            "history_farm_points",
            "total_score",
            "number_of_wins" "total_history_score",
        ]
