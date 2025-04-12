from peceras.models import Pecera, Temperatura, Sensor, PurezaAgua,CorrienteElectrica,Movimiento,NivelAgua,NivelOxigeno
from peceras.api.serializers import PeceraVS, TemperaturaS, SensoresSerializer, PurezaAguaS, CorrienteElectricaS, MovimientoS, NivelAguaS, NivelOxigenoS
from rest_framework import viewsets
from rest_framework import generics, mixins
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import  status

# Create your views here.
class PecerasVS(viewsets.ModelViewSet):
    queryset = Pecera.objects.all()
    serializer_class = PeceraVS

class TemperaturaPeceraListView(generics.ListCreateAPIView):
    serializer_class =  TemperaturaS

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Temperatura.objects.filter(fk_pecera = pk)
    


class PurezaAguaPeceraListView(generics.ListCreateAPIView):
    serializer_class =  PurezaAguaS

    def get_queryset(self):
        pk = self.kwargs['pk']
        return PurezaAgua.objects.filter(fk_pecera = pk)
    

class CorrienteElectricaListView(generics.ListCreateAPIView):
    serializer_class =  CorrienteElectricaS

    def get_queryset(self):
        pk = self.kwargs['pk']
        return CorrienteElectrica.objects.filter(fk_pecera = pk)

class MovimientoListView(generics.ListCreateAPIView):
    serializer_class =  MovimientoS

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Movimiento.objects.filter(fk_pecera = pk)

class NivelAguaListView(generics.ListCreateAPIView):
    serializer_class =  NivelAguaS

    def get_queryset(self):
        pk = self.kwargs['pk']
        return NivelAgua.objects.filter(fk_pecera = pk)


class NivelOxigenoListView(generics.ListCreateAPIView):
    serializer_class =  NivelOxigenoS

    def get_queryset(self):
        pk = self.kwargs['pk']
        return NivelOxigeno.objects.filter(fk_pecera = pk)

class Sensores(viewsets.ViewSet):
    def list(requeset, self):
        queryset = Sensor.objects.all()
        serializer = SensoresSerializer(queryset,many=True)
        return Response(serializer.data)

    def retrive(request, self, pk=None):
        queryset = Sensor.objects.all()
        sensor = get_object_or_404(queryset, pk = pk)
        serializer = SensoresSerializer(sensor)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = SensoresSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # faltaba el return

    def destroy(self, request, pk):
        try:
            sensor = Sensor.objects.get(pk=pk)  # corregido: get, no all
        
        except sensor.DoesNotExist:

            return Response({'error ' : 'sensor no encontrado'})

        sensor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


