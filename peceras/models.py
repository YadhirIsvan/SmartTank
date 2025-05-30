from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=128)  # puedes usar un método hash más adelante
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class TipoSensor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Sensor(models.Model):
    tipo = models.ForeignKey(TipoSensor, on_delete=models.CASCADE, related_name="sensores")

    def __str__(self):
        return f"Sensor {self.id} - Tipo: {self.tipo.nombre}"


class Pecera(models.Model):
    TAMAÑO_OPCIONES = [
        ('S', 'Pequeño'),
        ('M', 'Mediano'),
        ('G', 'Grande'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tamaño = models.CharField(max_length=1, choices=TAMAÑO_OPCIONES)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class RegistrosTemperatura(models.Model):
    pecera = models.ForeignKey(Pecera, on_delete=models.CASCADE, related_name="registros_temperatura")
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name="registros_temperatura")
    fecha = models.DateTimeField(auto_now_add=True)
    temperatura = models.FloatField()


class RegistrosCalidadAgua(models.Model):
    pecera = models.ForeignKey(Pecera, on_delete=models.CASCADE, related_name="registros_calidad")
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name="registros_calidad")
    fecha = models.DateTimeField(auto_now_add=True)
    calidad = models.FloatField()


class RegistrosMovimiento(models.Model):
    pecera = models.ForeignKey(Pecera, on_delete=models.CASCADE, related_name="registros_movimiento")
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name="registros_movimientos")
    fecha = models.DateTimeField(auto_now_add=True)
    movimiento = models.BooleanField()


class RegistrosNivelAgua(models.Model):
    pecera = models.ForeignKey(Pecera, on_delete=models.CASCADE, related_name="registros_nivelagua")
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name="registros_nivelagua")
    fecha = models.DateTimeField(auto_now_add=True)
    porcentaje = models.IntegerField()


class RegistrosFlujoAgua(models.Model):
    pecera = models.ForeignKey(Pecera, on_delete=models.CASCADE, related_name="registros_flujo")
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name="registros_flujo")
    fecha = models.DateTimeField(auto_now_add=True)
    flujo = models.IntegerField()


class RegistrosNivelOxigenoAgua(models.Model):
    pecera = models.ForeignKey(Pecera, on_delete=models.CASCADE, related_name="registros_oxigeno")
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name="registros_niveloxigeno")
    fecha = models.DateTimeField(auto_now_add=True)
    oxigeno_disuelto = models.FloatField()
