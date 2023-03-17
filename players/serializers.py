from rest_framework import serializers
from .models import Player


class PlayerSerializer(serializers.ModelSerializer):
    def update(self, instance: Player, validated_data: dict):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance

    class Meta:
        model = Player
        fields = [
            "id",
            "username",
            "max_street_points",
            "history_street_points",
            "max_city_points",
            "history_city_points",
            "max_monastery_points",
            "history_monastery_points",
            "max_farm_points",
            "history_farm_points",
            "max_total_score",
            "total_history_score",
            "number_of_wins",
        ]
        read_only_fields = [
            "max_street_points",
            "history_street_points",
            "max_city_points",
            "history_city_points",
            "max_monastery_points",
            "history_monastery_points",
            "max_farm_points",
            "history_farm_points",
            "max_total_score",
            "total_history_score",
            "number_of_wins",
        ]
