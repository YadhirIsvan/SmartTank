from django.urls import path
from .views import (
    ClienteListCreateView, ClienteDetailView,
    PeceraListCreateView, PeceraDetailView,
    RegistrosTemperaturaView, RegistrosTemperaturaDeleteView,
    RegistrosCalidadAguaView, RegistrosCalidadAguaDeleteView,
    RegistrosNivelOxigenoAguaView, RegistrosNivelOxigenoAguaDeleteView,
    RegistrosMovimientoView, RegistrosMovimientoDeleteView,
    RegistrosNivelAguaView, RegistrosNivelAguaDeleteView,
    RegistrosFlujoAguaView, RegistrosFlujoAguaDeleteView,
    SensorListCreateView, SensorRetrieveUpdateDestroyView,
    TipoSensorListCreateView, TipoSensorRetrieveUpdateDestroyView
)

urlpatterns = [

    # Clientes
    path('clientes/', ClienteListCreateView.as_view(), name='cliente-list'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),

    # Peceras
    path('peceras/', PeceraListCreateView.as_view(), name='pecera-list'),

    # Peceras
    path('peceras/<int:pk>/', PeceraDetailView.as_view(), name='pecera-detail'),

    # Registros
    path('registros/temperatura/', RegistrosTemperaturaView.as_view(), name='temperatura-list'),
    path('registros/temperatura/<int:pk>/', RegistrosTemperaturaDeleteView.as_view(), name='temperatura-delete'),

    path('registros/calidad/', RegistrosCalidadAguaView.as_view(), name='calidadagua-list'),
    path('registros/calidad/<int:pk>/', RegistrosCalidadAguaDeleteView.as_view(), name='calidadagua-delete'),

    path('registros/oxigeno/', RegistrosNivelOxigenoAguaView.as_view(), name='oxigeno-list'),
    path('registros/oxigeno/<int:pk>/', RegistrosNivelOxigenoAguaDeleteView.as_view(), name='oxigeno-delete'),

    path('registros/movimiento/', RegistrosMovimientoView.as_view(), name='movimiento-list'),
    path('registros/movimiento/<int:pk>/', RegistrosMovimientoDeleteView.as_view(), name='movimiento-delete'),

    path('registros/nivelagua/', RegistrosNivelAguaView.as_view(), name='nivelagua-list'),
    path('registros/nivelagua/<int:pk>/', RegistrosNivelAguaDeleteView.as_view(), name='nivelagua-delete'),

    path('registros/flujoagua/', RegistrosFlujoAguaView.as_view(), name='flujoagua-list'),
    path('registros/flujoagua/<int:pk>/', RegistrosFlujoAguaDeleteView.as_view(), name='flujoagua-delete'),

    path('sensores/', SensorListCreateView.as_view(), name='sensor-list-create'),
    path('sensores/<int:pk>/', SensorRetrieveUpdateDestroyView.as_view(), name='sensor-detail'),

     path('tiposensores/', TipoSensorListCreateView.as_view(), name='tipo-sensor-list-create'),
    path('tiposensores/<int:pk>/', TipoSensorRetrieveUpdateDestroyView.as_view(), name='tipo-sensor-detail'),
]
