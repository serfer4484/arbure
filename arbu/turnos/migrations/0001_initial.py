# Generated by Django 5.1.1 on 2024-09-10 15:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("empleados", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TurnosModel",
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
                ("Fecha_inicio", models.DateField()),
                ("Fecha_fin", models.DateField()),
                ("hora_inicio", models.TimeField()),
                ("hora_fin", models.TimeField()),
                (
                    "identifi",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="identifi",
                        to="empleados.empleadosmodels",
                    ),
                ),
            ],
        ),
    ]