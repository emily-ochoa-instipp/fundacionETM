from django.db import models

# Create your models here.

class Evento(models.Model):
    # TIPOS_EVENTO = [
    #     ('TALLER', 'Taller'),
    #     ('CHARLA', 'Charla'),
    #     ('CAMPAÑA', 'Campaña'),
    #     ('REUNIÓN', 'Reunión'),
    #     ('FERIA', 'Feria'),
    #     ('OTRO', 'Otro'),
    # ]


    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    # tipo = models.CharField(max_length=20, choices=TIPOS_EVENTO, default='OTRO')
    fecha = models.DateField()
    hora_inicio = models.TimeField(null=True, blank=True)
    hora_fin = models.TimeField(null=True, blank=True)
    lugar = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='eventos/', null=True, blank=True)
    #creado_en = models.DateTimeField(auto_now_add=True)
    #actualizado_en = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
