from django.db import models

class Pecera(models.Model):
    tamaño = models.CharField(max_length=50)
    cantidad_de_peces = models.IntegerField()

    def __str__(self):
        return f'Pecera {self.id} - Tamaño: {self.tamaño}'


class Sensor(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)
    fk_pecera = models.ForeignKey(Pecera, on_delete=models.CASCADE, related_name='sensores')

    def __str__(self):
        return f'{self.nombre} ({self.tipo}) - Pecera {self.fk_pecera.id}'


class Temperatura(models.Model):
    valor = models.FloatField()
    fecha_hora = models.DateTimeField()
    fk_pecera = models.ForeignKey(Pecera, on_delete=models.CASCADE, related_name='temperaturas')
    fk_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='temperaturas')

    def __str__(self):
        return f'{self.valor}°C - {self.fecha_hora}'


class PurezaAgua(models.Model):
    valor = models.IntegerField()
    fecha_hora = models.DateTimeField()
    fk_pecera = models.ForeignKey(Pecera, on_delete=models.CASCADE, related_name='purezas_agua')
    fk_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='purezas_agua')

    def __str__(self):
        return f'Pureza: {self.valor} - {self.fecha_hora}'


class CorrienteElectrica(models.Model):
    valor = models.BooleanField()
    fecha_hora = models.DateTimeField()
    fk_pecera = models.ForeignKey(Pecera, on_delete=models.CASCADE, related_name='corrientes_electricas')
    fk_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='corrientes_electricas')

    def __str__(self):
        return f'Corriente: {"Sí" if self.valor else "No"} - {self.fecha_hora}'


class Movimiento(models.Model):
    valor = models.BooleanField()
    fecha_hora = models.DateTimeField()
    fk_pecera = models.ForeignKey(Pecera, on_delete=models.CASCADE, related_name='movimientos')
    fk_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='movimientos')

    def __str__(self):
        return f'Movimiento: {"Sí" if self.valor else "No"} - {self.fecha_hora}'


class NivelAgua(models.Model):
    valor = models.IntegerField()
    fecha_hora = models.DateTimeField()
    fk_pecera = models.ForeignKey(Pecera, on_delete=models.CASCADE, related_name='niveles_agua')
    fk_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='niveles_agua')

    def __str__(self):
        return f'Nivel Agua: {self.valor} - {self.fecha_hora}'


class NivelOxigeno(models.Model):
    valor = models.FloatField()
    fecha_hora = models.DateTimeField()
    fk_pecera = models.ForeignKey(Pecera, on_delete=models.CASCADE, related_name='niveles_oxigeno')
    fk_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='niveles_oxigeno')

    def __str__(self):
        return f'Oxígeno: {self.valor} - {self.fecha_hora}'
