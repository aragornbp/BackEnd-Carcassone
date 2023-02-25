from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ["id", "created_at", "winner", "is_finish"]
        read_only_fields = ["id", "created_at", "winner", "is_finish"]
