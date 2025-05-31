from rest_framework import serializers
from peceras.models import Tamaño, Cliente, Pecera, \
    RegistrosNivelOxigenoAgua, RegistrosTemperatura, RegistrosCalidadAgua, \
    RegistrosMovimiento, RegistrosNivelAgua, RegistrosFlujoAgua


class TamañoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tamaño
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class PeceraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pecera
        fields = '__all__'


class RegistrosNivelOxigenoAguaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrosNivelOxigenoAgua
        fields = '__all__'


class RegistrosTemperaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrosTemperatura
        fields = '__all__'


class RegistrosCalidadAguaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrosCalidadAgua
        fields = '__all__'


class RegistrosMovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrosMovimiento
        fields = '__all__'


class RegistrosNivelAguaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrosNivelAgua
        fields = '__all__'


class RegistrosFlujoAguaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrosFlujoAgua
        fields = '__all__'
