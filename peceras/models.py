from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=128)
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
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tamano = models.TextField()  # Texto libre

    def __str__(self):
        return self.nombre

# ----------------------
# MODELOS CON try/except
# ----------------------

class RegistrosTemperatura(models.Model):
    pecera = models.ForeignKey(Pecera, on_delete=models.CASCADE, related_name="registros_temperatura")
    sensor = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    data = models.FloatField()

    @classmethod
    def create_safe(cls, pecera, sensor, data):
        try:
            return cls.objects.create(pecera=pecera, sensor=sensor, data=data)
        except Exception as e:
            print(f"[ERROR - RegistrosTemperatura] {e}")
            return None


class RegistrosCalidadAgua(models.Model):
    pecera = models.ForeignKey(Pecera, on_delete=models.CASCADE, related_name="registros_calidad")
    sensor = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    data = models.FloatField()

    @classmethod
    def create_safe(cls, pecera, sensor, data):
        try:
            return cls.objects.create(pecera=pecera, sensor=sensor, data=data)
        except Exception as e:
            print(f"[ERROR - RegistrosCalidadAgua] {e}")
            return None


class RegistrosMovimiento(models.Model):
    pecera = models.ForeignKey(Pecera, on_delete=models.CASCADE, related_name="registros_movimiento")
    sensor = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    data = models.BooleanField()

    @classmethod
    def create_safe(cls, pecera, sensor, data):
        try:
            return cls.objects.create(pecera=pecera, sensor=sensor, data=data)
        except Exception as e:
            print(f"[ERROR - RegistrosMovimiento] {e}")
            return None


class RegistrosNivelAgua(models.Model):
    pecera = models.ForeignKey(Pecera, on_delete=models.CASCADE, related_name="registros_nivelagua")
    sensor = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    data = models.IntegerField()

    @classmethod
    def create_safe(cls, pecera, sensor, data):
        try:
            return cls.objects.create(pecera=pecera, sensor=sensor, data=data)
        except Exception as e:
            print(f"[ERROR - RegistrosNivelAgua] {e}")
            return None


class RegistrosFlujoAgua(models.Model):
    pecera = models.ForeignKey(Pecera, on_delete=models.CASCADE, related_name="registros_flujo")
    sensor = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    data = models.IntegerField()

    @classmethod
    def create_safe(cls, pecera, sensor, data):
        try:
            return cls.objects.create(pecera=pecera, sensor=sensor, data=data)
        except Exception as e:
            print(f"[ERROR - RegistrosFlujoAgua] {e}")
            return None


class RegistrosNivelOxigenoAgua(models.Model):
    pecera = models.ForeignKey(Pecera, on_delete=models.CASCADE, related_name="registros_oxigeno")
    sensor = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    data = models.FloatField()

    @classmethod
    def create_safe(cls, pecera, sensor, data):
        try:
            return cls.objects.create(pecera=pecera, sensor=sensor, data=data)
        except Exception as e:
            print(f"[ERROR - RegistrosNivelOxigenoAgua] {e}")
            return None
