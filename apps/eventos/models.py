# from django.db import models
# from apps.usuarios.models import Usuario

# # Create your models here.

# class Paciente (models.Model):
#     usuario = models.OneToOneField('usuarios.Usuario', on_delete=models.CASCADE, null=True, blank=True)
#     fecha_nac = models.DateField(verbose_name='Fecha nacimiento', null=True, blank=True)
#     edad = models.IntegerField(null=True, blank=True)
#     sexo = models.CharField(max_length=10, null=True, blank=True)
#     tipo_sangre = models.CharField(max_length=3, null=True, blank=True, verbose_name='Tipo sangre')
#     direccion = models.CharField(max_length=255, null=True,  blank=True)
#     estado_civil = models.CharField(max_length=20, null=True, blank=True, verbose_name='Estado civil')
#     #estado = models.BooleanField(default=True)

#     def __str__(self):
#         return f"{self.usuario.user.first_name} {self.usuario.user.last_name}"

