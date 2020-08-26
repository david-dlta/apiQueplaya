from django.db import models

# Create your models here.

class Playa(models.Model):
    NOMBRE = models.CharField(max_length=30)
    CODIGO = models.CharField(max_length=15)
    LOCALIDAD = models.CharField(max_length=50)
    DESCRIPCION1 = models.CharField(max_length=500)
    FECHA_ALTA = models.DateTimeField(auto_now_add=True)
    FECHA_BAJA = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.NOMBRE
