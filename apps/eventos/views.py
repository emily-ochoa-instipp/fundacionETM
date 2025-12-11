from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.eventos.models import Evento, ImagenEvento

# Create your views here.

@login_required
def tabla_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/tabla_eventos.html', {
        'eventos': eventos
    })

def registrar_evento(request):
    
    if request.method == 'POST':
        titulo = request.POST.get('txtTitulo')
        descripcion = request.POST.get('txtDescripcion')
        fecha = request.POST.get('txtFecha')
        hora_inicio = request.POST.get('txtHoraInicio') 
        hora_fin = request.POST.get('txtHoraFin') 
        lugar = request.POST.get('txtLugar')
        direccion = request.POST.get('txtDireccion')
        imagen = request.FILES.get('txtImagen')

        estado = True  


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
                direccion=direccion,
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
        evento.titulo = request.POST.get('txtTitulo')
        evento.descripcion = request.POST.get('txtDescripcion')
        evento.fecha = request.POST.get('txtFecha')
        evento.hora_inicio = request.POST.get('txtHoraInicio')
        evento.hora_fin = request.POST.get('txtHoraFin') 
        evento.lugar = request.POST.get('txtLugar')
        evento.direccion = request.POST.get('txtDireccion')
        evento.estado = True if request.POST.get('estado') == 'on' else False
        
        #imagen portada
        if request.FILES.get('txtImagen'):
            evento.imagen = request.FILES['txtImagen']
        
        evento.save()
        
        return redirect('tabla_eventos')
    
    galeria = evento.galeria.all()

    return render(request, 'eventos/editar_evento.html', {'evento': evento, 'galeria': galeria})

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
