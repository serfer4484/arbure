from django.urls import path
from .views import EmpleadosFormView,EmpleadosListView,EmpleadosUpdateView,EmpleadosDeleteView



urlpatterns = [
    path('', EmpleadosListView.as_view(),name="lista_empleado"),
    path("agregar/",EmpleadosFormView.as_view(),name="empleados"),
    path('empleados/', EmpleadosListView.as_view(), name='lista_empleados'),
    path('empleados/editar/<int:pk>/', EmpleadosUpdateView.as_view(), name='editar_empleado'),
    path('empleados/eliminar/<int:pk>/', EmpleadosDeleteView.as_view(), name='eliminar_empleado'),
]
