# Generated by Django 4.1.7 on 2023-02-25 20:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Player",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=55, unique=True)),
                ("street_points", models.IntegerField(default=0)),
                ("history_street_points", models.IntegerField(default=0)),
                ("city_points", models.IntegerField(default=0)),
                ("history_city_points", models.IntegerField(default=0)),
                ("monastery_points", models.IntegerField(default=0)),
                ("history_monastery_points", models.IntegerField(default=0)),
                ("farm_points", models.IntegerField(default=0)),
                ("history_farm_points", models.IntegerField(default=0)),
                ("total_score", models.IntegerField(default=0)),
                ("number_of_wins", models.IntegerField(default=0)),
                ("total_history_score", models.IntegerField(default=0)),
            ],
        ),
    ]