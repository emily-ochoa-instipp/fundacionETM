from django.shortcuts import render, get_object_or_404

from django.core.paginator import Paginator
from django.utils import timezone
from apps.eventos.models import Evento, Proyecto


# Create your views here.

def index_views(request):
    # Solo mostrar los eventos que tienen estado=True
    eventos_visibles = Evento.objects.filter(estado=True)

    # Separar próximos y realizados según la fecha
    ahora = timezone.now()
    proximos = eventos_visibles.filter(fecha__gte=ahora).order_by('fecha')
    realizados = eventos_visibles.filter(fecha__lt=ahora).order_by('-fecha') [:6]

    context = {
        'proximos': proximos,
        'realizados': realizados,
    }

    return render(request, 'website/index.html', context)

def eventos_views(request):
    # Solo mostrar los eventos que tienen estado=True
    eventos_visibles = Evento.objects.filter(estado=True)
    ahora = timezone.now()
    realizados = eventos_visibles.filter(fecha__lt=ahora).order_by('-fecha')

    # PAGINACIÓN 6 eventos por página
    paginator = Paginator(realizados, 6)
    page_number = request.GET.get("page")
    realizados = paginator.get_page(page_number)


    context = {
        'realizados': realizados,
    }

    return render(request, 'website/eventos.html', context)

def evento_detalles(request, id):
    evento = get_object_or_404(Evento, id=id)
    return render(request, 'website/evento_detalles.html', {'evento': evento})


def proyecto_detalles(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    return render(request, 'website/proyecto_detalles.html', {'proyecto': proyecto})

