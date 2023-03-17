from rest_framework import serializers
from .models import Game, GamePlay
from players.models import Player


class GameSerializer(serializers.ModelSerializer):
    players = serializers.SerializerMethodField()

    def get_players(self, instance: Game) -> list:
        players_obj = GamePlay.objects.filter(game=instance)
        players_ids = [player.player_id for player in players_obj]
        players = []

        if players_ids:
            for player_id in players_ids:
                player: Player = Player.objects.filter(pk=player_id).first()
                game_play_obj = GamePlay.objects.filter(
                    game=instance, player_id=player_id
                ).first()
                players.append(
                    {
                        "id": player.id,
                        "username": player.username,
                        "total_score": game_play_obj.total_score,
                        "street_points": game_play_obj.street_points,
                        "monastery_points": game_play_obj.monastery_points,
                        "city_points": game_play_obj.city_points,
                        "farm_points": game_play_obj.farm_points,
                    }
                )
        return players

    class Meta:
        model = Game
        fields = ["id", "created_at", "winner", "is_finish", "players"]
        read_only_fields = ["id", "created_at", "winner", "is_finish", "players"]


class GamePlaySerializer(serializers.ModelSerializer):
    def update(self, instance: GamePlay, validated_data: dict):
        import ipdb

        ipdb.set_trace()
        for key, value in validated_data.items():
            if key == "street_points":
                instance.street_points += value
            if key == "city_points":
                instance.city_points += value
            if key == "monastery_points":
                instance.monastery_points += value
            if key == "farm_points":
                instance.farm_points += value

        instance.save()
        instance.total_score = (
            instance.street_points
            + instance.city_points
            + instance.monastery_points
            + instance.farm_points
        )
        instance.save()
        return instance

    class Meta:
        model = GamePlay
        fields = [
            "id",
            "player",
            "game",
            "street_points",
            "city_points",
            "monastery_points",
            "farm_points",
            "total_score",
        ]
        read_only_fields = [
            "id",
            "player",
            "game",
        ]
