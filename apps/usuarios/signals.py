from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from .models import Usuario

from django.conf import settings
from django.core.files import File
import os


# crea el perfil Usuario automáticamente cuando se crea el user

@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
    
        usuario = Usuario.objects.create(user=instance)

        if not usuario.foto:
            ruta_default = os.path.join(settings.BASE_DIR, 'static', 'assets', 'avatars', 'default.png')

            if os.path.exists(ruta_default):
                with open(ruta_default, 'rb') as img:
                    usuario.foto.save('default.png', File(img), save=True)

        grupo_defecto = "Secretaria" 

        # crea el grupo si no existe
        grupo, _ = Group.objects.get_or_create(name=grupo_defecto)

        # asigna el usuario al grupo
        instance.groups.add(grupo)

        # guarda el rol en el modelo usuario
        usuario.rol = grupo_defecto
        usuario.save()


@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs):
    if hasattr(instance, 'usuario'):
        instance.usuario.save()


#sicroniza el rol del modelo con el grupo de django
@receiver(post_save, sender=Usuario)
def sincronizar_rol_grupo(sender, instance, **kwargs):
 
    if instance.rol:
        grupo, _ = Group.objects.get_or_create(name=instance.rol)
        # limpia grupos anteriores
        instance.user.groups.clear()
        # agrega el grupo nuevo
        instance.user.groups.add(grupo)