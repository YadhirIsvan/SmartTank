from rest_framework import serializers
from peceras.models import Cliente, Pecera, \
    RegistrosNivelOxigenoAgua, RegistrosTemperatura, RegistrosCalidadAgua, \
    RegistrosMovimiento, RegistrosNivelAgua, RegistrosFlujoAgua



class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class PeceraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pecera
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

class RegistrosNivelOxigenoAguaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrosNivelOxigenoAgua
        fields = '__all__'

class PeceraSerializer(serializers.ModelSerializer):
    registros_temperatura = RegistrosTemperaturaSerializer(many=True, read_only=True)
    registros_calidad = RegistrosCalidadAguaSerializer(many=True, read_only=True)
    registros_movimiento = RegistrosMovimientoSerializer(many=True, read_only=True)
    registros_nivelagua = RegistrosNivelAguaSerializer(many=True, read_only=True)
    registros_flujo = RegistrosFlujoAguaSerializer(many=True, read_only=True)
    registros_oxigeno = RegistrosNivelOxigenoAguaSerializer(many=True, read_only=True)

    class Meta:
        model = Pecera
        fields = '__all__'
