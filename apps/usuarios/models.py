from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Usuario (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=30, default='Asistente')
    telefono = models.CharField(max_length=20, null=True, blank=True, verbose_name='Teléfono')
    num_doc = models.CharField(max_length=20, null=True, blank=True, verbose_name='N°Doc')
    foto = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.rol})"
