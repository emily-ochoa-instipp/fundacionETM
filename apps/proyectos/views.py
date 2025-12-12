from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Proyecto
from datetime import date

# Create your views here.

@login_required
def tabla_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyectos/tabla_proyectos.html', {
        'proyectos': proyectos
    })

def registrar_proyecto(request):
    if request.method == 'POST':
        nombre = request.POST.get('txtNombre')
        descripcion = request.POST.get('txtDescripcion')
        fecha_inicio = request.POST.get('txtFechaInicio')
        fecha_fin = request.POST.get('txtFechaFin') or None
        estado = True
        imagen = request.FILES.get('txtImagen')
        
        proyecto = Proyecto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            estado=estado,
            imagen=imagen
        )

        proyecto.save()
        return redirect('tabla_proyectos')
    return render(request, 'proyectos/tabla_proyectos.html')

@login_required
def editar_proyecto(request, proyecto_id):
    proyecto = Proyecto.objects.get(id=proyecto_id)

    if request.method == 'POST':
        proyecto.nombre = request.POST.get('txtNombre')
        proyecto.descripcion = request.POST.get('txtDescripcion')
        proyecto.fecha_inicio = request.POST.get('txtFechaInicio')
        proyecto.fecha_fin = request.POST.get('txtFechaFin')
        proyecto.estado = True if request.POST.get('estado') == 'on' else False

        if 'txtImagen' in request.FILES:
            proyecto.imagen = request.FILES('txtImagen')

        proyecto.save()
        

        return redirect('tabla_proyectos')

    return render(request, 'proyectos/editar_proyecto.html', {'proyecto': proyecto})

@login_required
def eliminar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id) 
    proyecto.delete()  
    
    return redirect('tabla_proyectos')
