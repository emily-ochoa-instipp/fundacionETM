from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Evento(models.Model):
    ESTADOS_EVENTO = [
        ('proximo', 'Próximo'),
        ('realizado', 'Realizado'),
        ('cancelado', 'Cancelado'),
    ]

    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha = models.DateField()
    hora_inicio = models.TimeField(null=True, blank=True)
    hora_fin = models.TimeField(null=True, blank=True)
    lugar = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    # imagen = models.ImageField(upload_to='eventos/imagen_portada', null=True, blank=True)
    imagen = CloudinaryField('imagen_portada', null=True, blank=True)
    estado =  models.CharField(max_length=15, choices=ESTADOS_EVENTO, default='proximo')

    def __str__(self):
        return self.titulo

class ImagenEvento(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="galeria")
    imagen_galeria = CloudinaryField('imagen_galeria')

    def __str__(self):
        return f"Imagen de {self.evento.titulo}"
