from django.db import models

class CategoriaDocumento(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class DocumentoTransparencia(models.Model):
    categoria = models.ForeignKey(CategoriaDocumento, on_delete=models.PROTECT, related_name='documentos')
    nombre = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='transparencia/')
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

