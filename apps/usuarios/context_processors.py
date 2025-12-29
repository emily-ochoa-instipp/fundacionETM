from apps.usuarios.models import Usuario

def usuario_actual(request):
    if request.user.is_authenticated:
        return {'usuario': request.user.usuario}  
