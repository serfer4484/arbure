from django.db import models


class RolModel(models.Model):
    roles=models.CharField(
        max_length=50,
        blank=False,
        null=False
    ) 

class EmpleadosModels(models.Model):
    nombres_empleado=models.CharField(
        max_length=200,
        blank=False,
        null=False
        )
    apellidos_empleado=models.CharField(
        max_length=200,
        blank=False,
        null=False)
    identificacion=models.IntegerField(
        blank=False,
        null=False,
        unique=True
    )
    sexo_empleado =models.CharField(
        max_length=20,
        blank=True, 
        null=True)
    telefono_empleado = models.CharField(
        max_length=10,
        blank=False, 
        null=False,
        )
    direccion_empleado=models.CharField(
        max_length=50,
        blank=False,
        null=False)
    email_empleado = models.EmailField(
        blank=False,
        null=False,
        unique=True)
    cargo_empleado = models.CharField(
        max_length=200,
        null=False,)
    salario_empleado = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=False, 
        null=False, 
        default=0.00) 
    contacto_emergencia=models.CharField(
        max_length=200,
        blank=False)
    tel_emergencia=models.CharField(
        max_length=10,
        blank=False,
          null=False,
          )
    foto_empleado = models.ImageField(
        upload_to='fotos_empleados/',
        blank=True, 
        null=True,   
        default='fotos_empleados/default.png'
        )
    rol_empleado = models.ForeignKey(
        RolModel,
        on_delete=models.DO_NOTHING,
        default=1,  # Suponiendo que el rol con ID 1 es el rol "Empleado"
        blank=False,
        null=False
    )
    def __str__(self):
        return self.nombres_empleado
