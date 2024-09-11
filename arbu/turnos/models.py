from django.db import models
from empleados.models import EmpleadosModels

class TurnosModel(models.Model):
    identifi=models.ForeignKey(
        EmpleadosModels,
        on_delete=models.CASCADE,
        related_name='identifi'
    )
    Fecha_inicio=models.DateField(
        null=False, 
        blank=False
    )
    Fecha_fin=models.DateField(
        null=False, 
        blank=False
    )
    hora_inicio=models.TimeField(
        null=False, 
        blank=False)
    hora_fin=models.TimeField(
        null=False, 
        blank=False
    )

