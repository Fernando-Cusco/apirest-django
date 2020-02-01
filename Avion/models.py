from django.db import models

# Create your models here.

class Avion(models.Model):

    aerolinea = models.CharField(max_length=100)
    fecha = models.DateField()
    precio = models.IntegerField(default = 100)
    descuento = models.IntegerField(default = 85)
