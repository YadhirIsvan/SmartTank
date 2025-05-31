from peceras.api.serializers import (
    ClienteSerializer,
    PeceraSerializer,
    RegistrosTemperaturaSerializer,
    RegistrosCalidadAguaSerializer,
    RegistrosNivelOxigenoAguaSerializer,
    RegistrosMovimientoSerializer,
    RegistrosNivelAguaSerializer,
    RegistrosFlujoAguaSerializer,
)


from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import  status

# 
from rest_framework import generics
from peceras.models import Cliente, Pecera, \
    RegistrosTemperatura, RegistrosCalidadAgua, RegistrosNivelOxigenoAgua, \
    RegistrosMovimiento, RegistrosNivelAgua, RegistrosFlujoAgua


# CRUD completo

class ClienteListCreateView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class PeceraListCreateView(generics.ListCreateAPIView):
    queryset = Pecera.objects.all()
    serializer_class = PeceraSerializer

class PeceraDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pecera.objects.all()
    serializer_class = PeceraSerializer


# Solo GET, POST, DELETE
class RegistrosTemperaturaView(generics.ListCreateAPIView):
    queryset = RegistrosTemperatura.objects.all()
    serializer_class = RegistrosTemperaturaSerializer

class RegistrosTemperaturaDeleteView(generics.DestroyAPIView):
    queryset = RegistrosTemperatura.objects.all()
    serializer_class = RegistrosTemperaturaSerializer


class RegistrosCalidadAguaView(generics.ListCreateAPIView):
    queryset = RegistrosCalidadAgua.objects.all()
    serializer_class = RegistrosCalidadAguaSerializer

class RegistrosCalidadAguaDeleteView(generics.DestroyAPIView):
    queryset = RegistrosCalidadAgua.objects.all()
    serializer_class = RegistrosCalidadAguaSerializer


class RegistrosNivelOxigenoAguaView(generics.ListCreateAPIView):
    queryset = RegistrosNivelOxigenoAgua.objects.all()
    serializer_class = RegistrosNivelOxigenoAguaSerializer

class RegistrosNivelOxigenoAguaDeleteView(generics.DestroyAPIView):
    queryset = RegistrosNivelOxigenoAgua.objects.all()
    serializer_class = RegistrosNivelOxigenoAguaSerializer


class RegistrosMovimientoView(generics.ListCreateAPIView):
    queryset = RegistrosMovimiento.objects.all()
    serializer_class = RegistrosMovimientoSerializer

class RegistrosMovimientoDeleteView(generics.DestroyAPIView):
    queryset = RegistrosMovimiento.objects.all()
    serializer_class = RegistrosMovimientoSerializer


class RegistrosNivelAguaView(generics.ListCreateAPIView):
    queryset = RegistrosNivelAgua.objects.all()
    serializer_class = RegistrosNivelAguaSerializer

class RegistrosNivelAguaDeleteView(generics.DestroyAPIView):
    queryset = RegistrosNivelAgua.objects.all()
    serializer_class = RegistrosNivelAguaSerializer


class RegistrosFlujoAguaView(generics.ListCreateAPIView):
    queryset = RegistrosFlujoAgua.objects.all()
    serializer_class = RegistrosFlujoAguaSerializer

class RegistrosFlujoAguaDeleteView(generics.DestroyAPIView):
    queryset = RegistrosFlujoAgua.objects.all()
    serializer_class = RegistrosFlujoAguaSerializer
