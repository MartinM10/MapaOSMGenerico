from django.db import models


# Create your models here.
class DatosGenerico(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    latitud = models.CharField(max_length=20)
    longitud = models.CharField(max_length=20)
