from rest_framework import serializers
from peceras.models import Pecera, Temperatura, Sensor, PurezaAgua, CorrienteElectrica,Movimiento,NivelAgua,NivelOxigeno


    
class TemperaturaS(serializers.ModelSerializer):

    class Meta:
        model = Temperatura
        fields = "__all__"

class SensoresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = "__all__"

class PurezaAguaS(serializers.ModelSerializer):

    class Meta:
        model = PurezaAgua
        fields = "__all__"


class CorrienteElectricaS(serializers.ModelSerializer):

    class Meta:
        model = CorrienteElectrica
        fields = "__all__"

class MovimientoS(serializers.ModelSerializer):

    class Meta:
        model = Movimiento
        fields = "__all__"


class NivelAguaS(serializers.ModelSerializer):

    class Meta:
        model = NivelAgua
        fields = "__all__"

class NivelOxigenoS(serializers.ModelSerializer):

    class Meta:
        model = NivelOxigeno
        fields = "__all__"

class PeceraVS(serializers.ModelSerializer):
# serializers.HyperlinkedModelSerializer
    temperaturas = TemperaturaS(many=True, read_only = True)
    purezas_agua = PurezaAguaS(many=True, read_only = True)
    corrientes_electricas = CorrienteElectricaS(many=True, read_only = True)
    movimientos = MovimientoS(many=True, read_only = True)
    niveles_agua = NivelAguaS(many=True, read_only = True)
    niveles_oxigeno = NivelOxigenoS(many=True, read_only = True)

    #edificacionlist = EdificacionSerializer(many = True, read_only = True)
    # edificacionserializer = serializers.StringRelatedField(many = True)


    # url = serializers.HyperlinkedIdentityField(view_name="empresa-detalle")  #  Asegura que DRF pueda generar la URL de Empresa


    # edificacionlist = serializers.HyperlinkedRelatedField(
    #     many = True,
    #     read_only = True, 
    #     view_name= 'detalles'
    # )

    class Meta:
        model = Pecera
        fields = "__all__"
        # fields = ['id', 'pais', 'activate', 'imagen']
        # exclude = ['id']