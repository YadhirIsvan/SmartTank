from peceras.api.serializers import (
    ClienteSerializer,
    PeceraSerializer,
    RegistrosTemperaturaSerializer,
    RegistrosCalidadAguaSerializer,
    RegistrosNivelOxigenoAguaSerializer,
    RegistrosMovimientoSerializer,
    RegistrosNivelAguaSerializer,
    RegistrosFlujoAguaSerializer,
    PecerasSerializer,
    SensorSerializer,
    TipoSensorSerializer
)
from rest_framework.views import APIView  # Asegúrate de tener esta importación



from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import  status

# 
from rest_framework import generics
from peceras.models import Cliente, Pecera, \
    RegistrosTemperatura, RegistrosCalidadAgua, RegistrosNivelOxigenoAgua, \
    RegistrosMovimiento, RegistrosNivelAgua, RegistrosFlujoAgua, Sensor, TipoSensor


# CRUD completo

class SensorListCreateView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class ClienteListCreateView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class PeceraListCreateView(generics.ListCreateAPIView):
    queryset = Pecera.objects.all()
    serializer_class = PecerasSerializer

# class PeceraDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Pecera.objects.all()
#     serializer_class = PeceraSerializer



# class PecerasListCreateView(generics.ListCreateAPIView):
#     queryset = Pecera.objects.all()
#     serializer_class = PecerasSerializer

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

class TipoSensorListCreateView(generics.ListCreateAPIView):
    queryset = TipoSensor.objects.all()
    serializer_class = TipoSensorSerializer

class TipoSensorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoSensor.objects.all()
    serializer_class = TipoSensorSerializer

    from rest_framework.views import APIView  # Asegúrate de tener esta importación

class EMQXReceiverView(APIView):
    def post(self, request):

        data= request.data.get('data', None)
        topic = request.data.get('topic', None)

        if (topic is None or data is None):
            #print("No se recibieron datos")
            return Response({"error": "No se recibieron datos"}, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     print("Topic ",topic, "Data", data)

        try:
            #PC/pecera/<idPecera>/<tipoSensor>/sensor/<idSensor>
            topic_parts = topic.split('/')
            idPecera = int(topic_parts[2])
            tipoSensor = topic_parts[3]
            idSensor = topic_parts[5]

            # if (idPecera == 4):
            #     print("Pecera 4 ", data)
            #print("ID Pecera:", idPecera, "Tipo Sensor:", tipoSensor, "ID Sensor:", idSensor)
            # return Response({"succes": "Datos recibidos correctamente"}, status=status.HTTP_200_OK)
        except Exception as e:
            #print("Error en el sensor ",tipoSensor)
            return Response({"error": "Formato erroneo"}, status=status.HTTP_400_BAD_REQUEST)
        
        pecera = Pecera.objects.get(pk=idPecera)  # id_pecera es un entero, p.ej. 3

        if (pecera is None):
            return Response({"error": "Pecera no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        # else:
        #     print("Pecera encontrada:", pecera.nombre)

        try:
            if tipoSensor == "temperatura":
                RegistrosTemperatura.create_safe(
                pecera=pecera,
                sensor=int(idSensor),
                data= int(data)
                
            )
                return Response({"success": "Registro de temperatura guardado correctamente"}, status=status.HTTP_201_CREATED) 
            if tipoSensor == "calidadAgua":
                RegistrosCalidadAgua.create_safe(
                pecera=pecera,
                sensor=int(idSensor),
                data= int(data)
            )
                return Response({"success": "Registro de calidad de agua guardado correctamente"}, status=status.HTTP_201_CREATED)
            if tipoSensor == "movimiento":
                RegistrosMovimiento.create_safe(
                pecera=pecera,
                sensor=int(idSensor),
                data=True
            ) 
                return Response({"success": "Registro de movimiento guardado correctamente"}, status=status.HTTP_201_CREATED)
            if tipoSensor == "nivelAgua":
                RegistrosNivelAgua.create_safe(
                pecera=pecera,
                sensor=int(idSensor),
                data= int(data)
            )
                return Response({"success": "Registro de nivel de agua guardado correctamente"}, status=status.HTTP_201_CREATED)
            if tipoSensor == "flujoAgua":
                RegistrosFlujoAgua.create_safe(
                pecera=pecera,
                sensor=int(idSensor),
                data= int(data)
            ) 
                return Response({"success": "Registro de flujo de agua guardado correctamente"}, status=status.HTTP_201_CREATED)
            if tipoSensor == "nivelOxigeno":
                RegistrosNivelOxigenoAgua.create_safe(
                pecera=pecera,
                sensor=int(idSensor),
                data= int(data)
            )
                return Response({"success": "Registro de oxigeno guardado correctamente"}, status=status.HTTP_201_CREATED)
                
            else:
                #print("Tipo de sensor no soportado:", tipoSensor)
                return Response({"error": "Tipo de sensor no soportado"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
                    return Response({"error": "Error al guardar el registro de temperatura"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)