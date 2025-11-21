from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from datetime import date
from django.utils import timezone
from apps.eventos.models import Evento
from apps.proyectos.models import Proyecto
from apps.usuarios.models import Usuario


# Create your views here.

@login_required
def inicio(request):
    return render(request, 'inicio/inicio.html')

@login_required
def inicio(request):
    # total_voluntarios = Voluntario.objects.count()
    proyectos_activos = Proyecto.objects.filter(estado=True).count()
    usuarios_activos = Usuario.objects.filter(user__is_active=True).count()
    eventos_hoy = Evento.objects.filter(fecha=date.today()).count()
    eventos_proximos = Evento.objects.filter(fecha__gte=timezone.now()).count()
    # eventos_proximos = Evento.objects.filter(fecha__gte=date.today()).order_by('fecha')
 


    context = {
        # 'total_voluntarios': total_voluntarios,
        'proyectos_activos': proyectos_activos,
        'usuarios_activos': usuarios_activos,
        'eventos_hoy': eventos_hoy,
        'eventos_proximos': eventos_proximos,
    }

    return render(request, 'inicio/inicio.html', context)