from django.db import models

class DocumentoTransparencia(models.Model):

    nombre = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='transparencia/')
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
