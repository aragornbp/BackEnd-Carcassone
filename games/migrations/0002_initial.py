# Generated by Django 4.1.7 on 2023-03-16 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("players", "0001_initial"),
        ("games", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="gameplay",
            name="player",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="gameplay",
                to="players.player",
            ),
        ),
        migrations.AddField(
            model_name="game",
            name="players",
            field=models.ManyToManyField(
                related_name="game", through="games.GamePlay", to="players.player"
            ),
        ),
    ]
