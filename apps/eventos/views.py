from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from apps.eventos.models import Evento
from datetime import date

# Create your views here.

@login_required
def tabla_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/tabla_eventos.html', {
        'eventos': eventos
    })

def registrar_evento(request):
    error = None
    if request.method == 'POST':
        titulo = request.POST['txtTitulo']
        descripcion = request.POST['txtDescripcion']
        fecha = request.POST['txtFecha']
        hora_inicio = request.POST['txtHoraInicio'] or None
        hora_fin = request.POST['txtHoraFin'] or None
        lugar = request.POST['txtLugar']
        imagen = request.FILES.get('imagen')
        estado = request.POST.get('txtEstado') == 'on'

        if not (titulo and descripcion and fecha):
            error = "Todos los campos son obligatorios"
        else:
            Evento.objects.create(
                titulo=titulo,
                descripcion=descripcion,
                fecha=fecha,
                hora_inicio=hora_inicio,
                hora_fin=hora_fin,
                lugar=lugar,
                imagen=imagen,
                estado=estado
            )
            return redirect('tabla_eventos')

    eventos = Evento.objects.all()
    return render(request, 'eventos/tabla_eventos.html', {
        'error': error,
        'eventos': eventos
    })


@login_required
def editar_evento(request, evento_id):
    evento = Evento.objects.get(id=evento_id)

    if request.method == 'POST':
        evento.titulo = request.POST['txtTitulo']
        evento.descripcion = request.POST['txtDescripcion']
        evento.fecha = request.POST['txtFecha']
        evento.hora_inicio = request.POST['txtHoraInicio']
        evento.hora_fin = request.POST['txtHoraFin']
        evento.lugar = request.POST['txtLugar']
        evento.estado = request.POST['txtEstado']

        if 'txtImagen' in request.FILES:
            evento.imagen = request.FILES['txtImagen']
        
        evento.save()
        
        return redirect('tabla_eventos')

    return render(request, 'eventos/editar_evento.html', {'evento': evento})

@login_required
def eliminar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    
    evento.delete()   
    return redirect('tabla_eventos')

