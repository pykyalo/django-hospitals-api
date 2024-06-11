# Generated by Django 4.2.13 on 2024-06-11 10:48

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hospital",
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
                ("name", models.CharField(max_length=255, verbose_name="Name")),
                ("lo", models.FloatField(verbose_name="Longitude")),
                ("la", models.FloatField(verbose_name="Latitude")),
                ("fi", models.IntegerField(verbose_name="Field ID")),
                ("beds", models.IntegerField(default=1, verbose_name="Bed Numbers")),
                (
                    "province_name",
                    models.CharField(max_length=100, verbose_name="Province Name"),
                ),
                (
                    "province_code",
                    models.CharField(max_length=1, verbose_name="Province Code"),
                ),
                ("geom", django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                "verbose_name": "Hospitals",
                "verbose_name_plural": "Hospitals",
            },
        ),
    ]
