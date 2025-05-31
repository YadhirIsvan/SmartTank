from django.db import models

class Tamaño(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=128)  # puedes usar un método hash más adelante
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre


class Pecera(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tamaño = models.ForeignKey(Tamaño, on_delete=models.SET_NULL, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class RegistrosTemperatura(models.Model):
    pecera = models.ForeignKey(Pecera, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    temperatura = models.FloatField()
    sensor = models.IntegerField()


class RegistrosFlujoAgua(models.Model):
    pecera = models.ForeignKey(Pecera, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    flujo = models.IntegerField()
    sensor = models.IntegerField()


class RegistrosMovimiento(models.Model):
    pecera = models.ForeignKey(Pecera, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    movimiento = models.BooleanField()
    sensor = models.IntegerField()


class RegistrosCalidadAgua(models.Model):
    pecera = models.ForeignKey(Pecera, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    calidad = models.FloatField()
    sensor = models.IntegerField()


class RegistrosNivelAgua(models.Model):
    pecera = models.ForeignKey(Pecera, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    porcentaje = models.IntegerField()
    sensor = models.IntegerField()


class RegistrosNivelOxigenoAgua(models.Model):
    pecera = models.ForeignKey(Pecera, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    oxigeno_disuelto = models.FloatField()
    sensor = models.IntegerField()