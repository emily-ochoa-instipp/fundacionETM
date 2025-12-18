from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import date

from apps.eventos.models import Evento
from apps.proyectos.models import Proyecto
from apps.usuarios.models import Usuario


@login_required
def inicio(request):
    hoy = date.today()

    # PROYECTOS
    proyectos_activos = Proyecto.objects.filter(estado='en_curso').count()
    proyectos_realizados = Proyecto.objects.filter(estado='realizado').count()

    # EVENTOS
    eventos_realizados = Evento.objects.filter(estado='realizado').count()
    eventos_proximos = Evento.objects.filter(fecha__gte=hoy, estado='proximo').count()

    # USUARIOS
    usuarios_activos = Usuario.objects.filter(user__is_active=True).count()

    context = {
        'proyectos_activos': proyectos_activos,
        'proyectos_realizados': proyectos_realizados,
        'usuarios_activos': usuarios_activos,
        'eventos_realizados': eventos_realizados,
        'eventos_proximos': eventos_proximos,
    }

    return render(request, 'inicio/inicio.html', context)
