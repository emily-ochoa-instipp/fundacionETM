from django.db import models
from cloudinary.models import CloudinaryField


class MujerReferente(models.Model):
    nombre = models.CharField(max_length=150)
    lugar_origen = models.CharField(max_length=150,)
    ocupacion = models.CharField(max_length=150,)
    descripcion = models.TextField()
    imagen = CloudinaryField('mujer_referente', null=True, blank=True,)
    # imagen = models.ImageField(upload_to="mujeres_referentes/", null=True, blank=True,)
    estado = models.BooleanField(default=True, verbose_name="Activo")

    def __str__(self):
        return self.nombre
