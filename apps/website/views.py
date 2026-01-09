from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.utils import timezone
from django.db.models import Case, When, Value, IntegerField
from apps.transparencia.models import CategoriaDocumento
from apps.eventos.models import Evento
from apps.proyectos.models import Proyecto
from apps.mujeres_referentes.models import MujerReferente
from apps.miembros.models import Miembro  

def index_views(request):

    ahora = timezone.now()

    # EVENTOS
    actualizar_estados_eventos()
    proximos_eventos = Evento.objects.filter(estado='proximo', fecha__gte=ahora.date()).order_by('fecha')
    eventos_realizados = Evento.objects.filter(estado='realizado', fecha__lt=ahora.date()).order_by('-fecha')[:6]

    # PROYECTOS
    actualizar_estados_proyectos()
    proyectos_en_curso = Proyecto.objects.filter(estado='en_curso').order_by('-fecha_inicio')
    proyectos_realizados = Proyecto.objects.filter(estado='realizado').order_by('-fecha_fin')[:6]
    
    #MUJERES REFERENTES
    mujeres_referentes = MujerReferente.objects.filter(estado=True)

    #Categorias transparencia-menu
    menu_categorias = CategoriaDocumento.objects.prefetch_related('documentos').all()

    #MIEMBROS DE LA FUNDACION
    miembros = Miembro.objects.filter(estado=True).annotate(
        orden=Case(
            When(cargo='presidenta', then=Value(1)),
            When(cargo='secretaria', then=Value(2)),
            When(cargo='tesorera', then=Value(3)),
            When(cargo='socia', then=Value(4)),
            default=Value(5),
            output_field=IntegerField(),
        )
    ).order_by('orden', 'apellido')


    context = {
        'proximos_eventos': proximos_eventos,
        'eventos_realizados': eventos_realizados,
        'proyectos_en_curso': proyectos_en_curso,
        'proyectos_realizados': proyectos_realizados,
        'mujeres_referentes': mujeres_referentes,
        'miembros': miembros, 
        'menu_categorias': menu_categorias, 
    }

    return render(request, 'website/index.html', context)

#eventos

def actualizar_estados_eventos():
    Evento.objects.filter(fecha__lt=timezone.now().date(), estado='proximo').update(estado='realizado')

def eventos_views(request):
    actualizar_estados_eventos()

    realizados = Evento.objects.filter(estado='realizado').order_by('-fecha')

    # PAGINACIÓN 6 evetnos por pagina
    paginator = Paginator(realizados, 6)
    page_number = request.GET.get("page")
    realizados = paginator.get_page(page_number)

    context = {
        'realizados': realizados,
    }

    return render(request, 'website/eventos.html', context)

def evento_detalles(request, id):
    evento = get_object_or_404(Evento, id=id, )
    return render(request, 'website/evento_detalles.html', {'evento': evento})

#PROYECTOS

def actualizar_estados_proyectos():
    Proyecto.objects.filter(fecha_fin__lt=timezone.now().date(), estado='en_curso').update(estado='realizado')

#realizado---------------------

def proyectos_realizados_views(request):
    actualizar_estados_proyectos()

    realizados = Proyecto.objects.filter(estado='realizado').order_by('-fecha_fin')

    # PAGINACIÓN
    paginator = Paginator(realizados, 6)
    page_number = request.GET.get("page")
    realizados = paginator.get_page(page_number)

    context = {
        'realizados': realizados,
    }

    return render(request, 'website/proyectos_realizados.html', context)

def proyecto_realizado_detalles(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    return render(request, 'website/proyecto_realizado_detalles.html', {'proyecto': proyecto})

#en curso---------------------
def proyectos_en_curso_views(request):
    actualizar_estados_proyectos()

    en_curso = Proyecto.objects.filter(estado='en_curso').order_by('-fecha_inicio')

    # PAGINACIÓN
    paginator = Paginator(en_curso, 6)
    page_number = request.GET.get("page")
    en_curso = paginator.get_page(page_number)

    context = {
        'en_curso': en_curso
    }

    return render(request, 'website/proyectos_en_curso.html', context)

def proyecto_en_curso_detalles(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    return render(request, 'website/proyecto_en_curso_detalles.html', {'proyecto': proyecto})

