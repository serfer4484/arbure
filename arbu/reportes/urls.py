from django.urls import path
from .views import DEscargarResporteEmpleadosView,ReporteEmpleadosView

urlpatterns = [
    path('', ReporteEmpleadosView.as_view(), name='reporteEmpleados'),
    path('descargar/', DEscargarResporteEmpleadosView.as_view(), name='descargarReporteEmpleados'),
]