from django.contrib import admin
from .models import Pecera, Sensor, Temperatura, PurezaAgua, CorrienteElectrica, Movimiento, NivelAgua, NivelOxigeno

# Registrar los modelos en el admin
admin.site.register(Pecera)
admin.site.register(Sensor)
admin.site.register(Temperatura)
admin.site.register(PurezaAgua)
admin.site.register(CorrienteElectrica)
admin.site.register(Movimiento)
admin.site.register(NivelAgua)
admin.site.register(NivelOxigeno)
