from django.contrib import admin
from .models import EmpleadosModels

# Register your models here.
class EmpleadosAdmin(admin.ModelAdmin):
    model = EmpleadosModels
    list_display = ['nombres_empleado','apellidos_empleado','telefono_empleado']
    search_fields = ['identificacion']
    admin.site.register(EmpleadosModels) 

