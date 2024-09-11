from django.urls import path
from .views import NovedadesFormViews,NovedadesListView

urlpatterns = [
    path('',NovedadesFormViews.as_view(),name='novedades' ),
    path('lista/', NovedadesListView.as_view(), name='lista_novedades'),
]