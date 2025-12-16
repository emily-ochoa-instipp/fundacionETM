from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.eventos.models import Evento, ImagenEvento
from datetime import date

# Create your views here.

@login_required
def tabla_eventos(request):
    eventos = Evento.objects.all().order_by('-fecha')
    return render(request, 'eventos/tabla_eventos.html', {
        'eventos': eventos
    })

@login_required
def registrar_evento(request):
    error = None
    
    if request.method == 'POST':
        titulo = request.POST.get('txtTitulo')
        descripcion = request.POST.get('txtDescripcion')
        fecha_str = request.POST.get('txtFecha')
        hora_inicio = request.POST.get('txtHoraInicio') 
        hora_fin = request.POST.get('txtHoraFin') 
        lugar = request.POST.get('txtLugar')
        direccion = request.POST.get('txtDireccion')
        imagen = request.FILES.get('txtImagen')
        estado_form = request.POST.get('estado')

        if not (titulo and descripcion and fecha_str):
            error = "Todos los campos son obligatorios"
        else:
            fecha = date.fromisoformat(fecha_str)
            hoy = date.today()

            if estado_form == 'cancelado':
                estado_final = 'cancelado'
            elif estado_form == 'realizado':
                estado_final = 'realizado'
            else:
                estado_final = 'realizado' if fecha < hoy else 'proximo'
            
            Evento.objects.create(
                titulo=titulo,
                descripcion=descripcion,
                fecha=fecha,
                hora_inicio=hora_inicio,
                hora_fin=hora_fin,
                lugar=lugar,
                direccion=direccion,
                imagen=imagen,
                estado=estado_final
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

    error = None 

    if request.method == 'POST':
        evento.titulo = request.POST.get('txtTitulo')
        evento.descripcion = request.POST.get('txtDescripcion')

        fecha_str = request.POST.get('txtFecha')
        fecha = date.fromisoformat(fecha_str)
        evento.fecha = fecha
        
        evento.hora_inicio = request.POST.get('txtHoraInicio')
        evento.hora_fin = request.POST.get('txtHoraFin') 
        evento.lugar = request.POST.get('txtLugar')
        evento.direccion = request.POST.get('txtDireccion')
        estado_form = request.POST.get('estado')

        hoy = date.today()

        if estado_form == 'proximo' and evento.fecha < hoy:
            error = "No puedes marcar como próximo un evento cuya fecha ya pasó."

        elif estado_form == 'realizado' and evento.fecha > hoy:
            error = "No puedes marcar como realizado un evento con fecha futura."

        else:
            evento.estado = estado_form
        
            #imagen portada
            if request.FILES.get('txtImagen'):
                evento.imagen = request.FILES['txtImagen']
            
            evento.save()
            
            return redirect('tabla_eventos')
    
    galeria = evento.galeria.all()

    return render(request, 'eventos/editar_evento.html', {'evento': evento, 'galeria': galeria, 'error': error,'Evento': Evento})

@login_required
def eliminar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    
    evento.delete()   
    return redirect('tabla_eventos')


@login_required
def agregar_imagen_galeria(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    if request.method == "POST":
        imagenes = request.FILES.getlist("imagenes")  

        for img in imagenes:
            ImagenEvento.objects.create(
                evento=evento,
                imagen_galeria=img,
            )

        return redirect("editar_evento", evento_id=evento.id)

    return render(request, "eventos/tabla_eventos.html", {"evento": evento})

@login_required
def eliminar_imagen_galeria(request, imagen_id):
    imagen = get_object_or_404(ImagenEvento, id=imagen_id)
    evento_id = imagen.evento.id
    imagen.delete()
    return redirect("editar_evento", evento_id=evento_id)
