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
        nombre = request.POST['txtNombre']
        descripcion = request.POST['txtDescripcion']
        fecha_inicio = request.POST['txtFechaInicio']
        estado = request.POST['txtEstado']
        imagen = request.FILES.get('txtImagen')
        
        Proyecto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            fecha_inicio=fecha_inicio,
            estado=estado,
            imagen=imagen
        )
        return redirect('tabla_proyectos')
    return render(request, 'proyectos/tabla_proyectos.html')

@login_required
def editar_proyecto(request, proyecto_id):
    proyecto = Proyecto.objects.get(id=proyecto_id)

    if request.method == 'POST':
        proyecto.nombre = request.POST['txtNombre']
        proyecto.descripcion = request.POST['txtDescripcion']
        proyecto.fecha_inicio = request.POST['txtFechaInicio']
        proyecto.estado = request.POST['txtEstado']

        if 'txtImagen' in request.FILES:
            proyecto.imagen = request.FILES['txtImagen']
        proyecto.save()
        

        return redirect('tabla_proyectos')

    return render(request, 'proyectos/editar_proyecto.html', {'proyecto': proyecto})

@login_required
def eliminar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id) 
    proyecto.delete()  
    
    return redirect('tabla_proyectos')
