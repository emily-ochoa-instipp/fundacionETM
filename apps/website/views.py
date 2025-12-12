from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.utils import timezone

from apps.eventos.models import Evento
from apps.proyectos.models import Proyecto


def index_views(request):
    eventos_visibles = Evento.objects.filter(estado=True)
    proyectos_visibles = Proyecto.objects.filter(estado=True)

    ahora = timezone.now()

    # EVENTOS
    proximos_eventos = eventos_visibles.filter(fecha__gte=ahora).order_by('fecha')
    eventos_realizados = eventos_visibles.filter(fecha__lt=ahora).order_by('-fecha')[:6]

    # PROYECTOS
    proyectos_en_curso = proyectos_visibles.filter(
        fecha_fin__isnull=True
    ) | proyectos_visibles.filter(fecha_fin__gte=ahora)

    proyectos_realizados = proyectos_visibles.filter(
        fecha_fin__lt=ahora
    ).order_by('-fecha_fin')[:6]

    context = {
        'proximos': proximos_eventos,
        'realizados': eventos_realizados,
        'proyectos_en_curso': proyectos_en_curso,
        'proyectos_realizados': proyectos_realizados,
    }

    return render(request, 'website/index.html', context)


def eventos_views(request):
    eventos_visibles = Evento.objects.filter(estado=True)
    ahora = timezone.now()

    realizados = eventos_visibles.filter(fecha__lt=ahora).order_by('-fecha')

    # PAGINACIÓN 6 evetnos por pagina
    paginator = Paginator(realizados, 6)
    page_number = request.GET.get("page")
    realizados = paginator.get_page(page_number)

    context = {
        'realizados': realizados,
    }

    return render(request, 'website/eventos.html', context)


def proyectos_views(request):
    proyectos_visibles = Proyecto.objects.filter(estado=True)
    ahora = timezone.now()

    realizados = proyectos_visibles.filter(
        fecha_fin__lt=ahora
    ).order_by('-fecha_fin')

    # PAGINACIÓN
    paginator = Paginator(realizados, 6)
    page_number = request.GET.get("page")
    realizados = paginator.get_page(page_number)

    context = {
        'realizados': realizados,
    }

    return render(request, 'website/proyectos.html', context)


def evento_detalles(request, id):
    evento = get_object_or_404(Evento, id=id)
    return render(request, 'website/evento_detalles.html', {'evento': evento})

def proyecto_detalles(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    return render(request, 'website/proyecto_detalles.html', {'proyecto': proyecto})
