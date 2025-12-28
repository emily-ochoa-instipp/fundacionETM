from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import date

from apps.eventos.models import Evento
from apps.proyectos.models import Proyecto
from apps.usuarios.models import Usuario
from apps.usuarios.decorators import roles_permitidos


@login_required
@user_passes_test(roles_permitidos(['Secretaria', 'Presidenta','Administrador']))

def inicio(request):
    hoy = date.today()

    # PROYECTOS
    proyectos_activos = Proyecto.objects.filter(estado='en_curso')
    proyectos_activos_count = proyectos_activos.count()

    proyectos_realizados = Proyecto.objects.filter(estado='realizado')
    proyectos_realizados_count = proyectos_realizados.count()

    # EVENTOS
    eventos_realizados = Evento.objects.filter(estado='realizado')
    eventos_realizados_count = eventos_realizados.count()

    eventos_proximos = Evento.objects.filter(fecha__gte=hoy, estado='proximo')
    eventos_proximos_count = eventos_proximos.count()

    # USUARIOS
    usuarios_activos = Usuario.objects.filter(user__is_active=True)
    usuarios_activos_count = usuarios_activos.count()

    context = {
        'proyectos_activos': proyectos_activos,
        'proyectos_activos_count': proyectos_activos_count,
        'proyectos_realizados': proyectos_realizados,
        'proyectos_realizados_count': proyectos_realizados_count,
        'usuarios_activos': usuarios_activos,
        'usuarios_activos_count': usuarios_activos_count,
        'eventos_realizados': eventos_realizados,
        'eventos_realizados_count': eventos_realizados_count,
        'eventos_proximos': eventos_proximos,
        'eventos_proximos_count': eventos_proximos_count,
    }

    return render(request, 'inicio/inicio.html', context)

