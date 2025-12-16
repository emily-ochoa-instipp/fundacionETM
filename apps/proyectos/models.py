from django.db import models

# Create your models here.

class Proyecto (models.Model):
    ESTADOS_PROYECTO = [
        ('en_curso', 'En curso'),
        ('realizado', 'Realizado'),
        ('cancelado', 'Cancelado'),
    ]

    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='proyectos/imagen_portada', blank=True, null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS_PROYECTO, default='en_curso')

    def __str__(self):
        return self.nombre

class ImagenProyecto(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="galeria")
    imagen_galeria = models.ImageField(upload_to='proyectos/galeria/')

    def __str__(self):
        return f"Imagen de {self.proyecto.titulo}"
