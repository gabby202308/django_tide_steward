# Generated by Django 4.0.3 on 2022-03-30 18:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shifts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shift",
            name="lowest_tide",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="shift",
            name="mllw_feet",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="shift",
            name="sunrise",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="shift",
            name="sunset",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
