from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PecerasVS, TemperaturaPeceraListView, Sensores, PurezaAguaPeceraListView, CorrienteElectricaListView, MovimientoListView, NivelOxigenoListView

router = DefaultRouter()
router.register(r'peceras', PecerasVS, basename='peceras')
router.register(r'sensores', Sensores, basename='sensores')  

urlpatterns = [
    path('', include(router.urls)),
    path('peceras/<int:pk>/temperatura/', TemperaturaPeceraListView.as_view(), name="temperatura"),
    path('peceras/<int:pk>/pureza/', PurezaAguaPeceraListView.as_view(), name="pureza_agua"),
    path('peceras/<int:pk>/corrienteelectrica/', CorrienteElectricaListView.as_view(), name="corriente_electrica"),
    path('peceras/<int:pk>/movimiento/', MovimientoListView.as_view(), name="movimiento"),
    path('peceras/<int:pk>/niveloxigeno/', NivelOxigenoListView.as_view(), name="nivel_oxigeno"),
]
