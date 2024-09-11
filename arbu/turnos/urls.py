from django.urls import path
from .views import TurnosViews,TurnosSemanaView

urlpatterns = [
    path('',TurnosViews.as_view(),name='turnos' ),
    path('lista-turnos-semana/', TurnosSemanaView.as_view(), name='lista_turnos_semana'),
]

