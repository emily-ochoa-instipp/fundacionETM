from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.utils import timezone
from apps.eventos.models import Evento


# Create your views here.

def index_views(request):
    # Solo mostrar los eventos que tienen estado=True
    eventos_visibles = Evento.objects.filter(estado=True)

    # Separar próximos y realizados según la fecha
    ahora = timezone.now()
    proximos = eventos_visibles.filter(fecha__gte=ahora).order_by('fecha')
    realizados = eventos_visibles.filter(fecha__lt=ahora).order_by('-fecha')

    context = {
        'proximos': proximos,
        'realizados': realizados,
    }

    return render(request, 'website/index.html', context)