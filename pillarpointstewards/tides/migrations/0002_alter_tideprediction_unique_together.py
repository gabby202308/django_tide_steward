# Generated by Django 4.0.3 on 2022-04-02 23:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tides", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="tideprediction",
            unique_together={("station_id", "dt")},
        ),
    ]
