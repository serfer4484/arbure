from django.db import models
from empleados.models import EmpleadosModels

class TipoNovedadModel(models.Model): 
    Tipo_novedad=models.TextField(
        max_length=50,
        blank=False,
        null=False
        )

class NovedadesModel(models.Model):
    iden=models.ForeignKey(
        EmpleadosModels,
        on_delete=models.CASCADE,
        related_name='iden'
    ) 
    nombres_empleado=models.TextField(
        max_length=200,
        blank=False,
        null=False)
    apellidos_empleado=models.TextField(
        max_length=200,
        blank=False,
        null=False)
    novedad_empleado=models.ForeignKey(
        TipoNovedadModel,
        on_delete=models.CASCADE,
        default=1,
        blank=False,
        null=False        
    )
    Fecha_inicio=models.DateField(
        null=False, 
        blank=False
    )
    Fecha_fin=models.DateField(
        null=False, 
        blank=False
    )
    soporte=models.FileField(
        upload_to='soportes/',
        blank=False,
        null=False,
    )




