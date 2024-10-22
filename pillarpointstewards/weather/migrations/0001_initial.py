# Generated by Django 4.0.3 on 2022-04-02 18:47

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Forecast",
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
                ("date", models.DateField(db_index=True)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("details", models.JSONField()),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]