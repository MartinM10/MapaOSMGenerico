from django.db import models


# Create your models here.
class DatosGenerico(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)
    latitud = models.CharField(max_length=20, null=False, blank=False)
    longitud = models.CharField(max_length=20, null=False, blank=False)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
