from django.db import models


class Miembro(models.Model):
    CARGO_CHOICES = [
        ('presidenta', 'Presidenta'),
        ('secretaria', 'Secretaria'),
        ('tesorera', 'Tesorera'),
        ('socia', 'Socia'),
    ]

    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    descripcion = models.TextField()
    cargo = models.CharField(max_length=20, choices=CARGO_CHOICES)
    foto = models.ImageField(upload_to='miembros/', blank=True, null=True)
    estado = models.BooleanField(default=True)  

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

