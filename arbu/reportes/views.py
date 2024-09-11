from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import openpyxl
from empleados.models import EmpleadosModels

class ReporteEmpleadosView(View):
    def get(self, request):
        return render(request, 'reportes/reporte.html')

class DEscargarResporteEmpleadosView(View):
    def get(self, request, *args, **kwargs):
        # Crear un libro de trabajo y una hoja
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.title = 'Reporte de Empleados'

        # Definir los encabezados de las columnas
        columns = ['ID',
                    'Nombres',
                    'Apellidos',
                    'identificación',
                    'Sexo',
                    'Teléfono',
                    'Dirección',
                    'Correo Electrónico',
                    'Cargo',
                    'Salario'
                    ]
        worksheet.append(columns)

        # Obtener los datos de los empleados
        empleados = EmpleadosModels.objects.all()

        for empleado in empleados:
            worksheet.append([
                empleado.id,
                empleado.nombres_empleado,
                empleado.apellidos_empleado,
                empleado.identificacion,
                empleado.sexo_empleado,  
                empleado.telefono_empleado,
                empleado.direccion_empleado,            
                empleado.email_empleado,
                empleado.cargo_empleado,
                empleado.salario_empleado
            ])

        # Crear una respuesta HTTP con el archivo Excel
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=empleados.xlsx'

        # Guardar el libro de trabajo en la respuesta
        workbook.save(response)
        return response

