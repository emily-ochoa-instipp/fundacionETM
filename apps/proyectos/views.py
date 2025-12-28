from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Proyecto, ImagenProyecto
from datetime import date
from apps.usuarios.decorators import roles_permitidos

# Create your views here.

@login_required
@user_passes_test(roles_permitidos(['Secretaria', 'Presidenta','Administrador', 'Socia']))

def tabla_proyectos(request):
    proyectos = Proyecto.objects.all().order_by('-fecha_inicio')
    return render(request, 'proyectos/tabla_proyectos.html', {
        'proyectos': proyectos
    })

@login_required
@user_passes_test(roles_permitidos(['Secretaria', 'Presidenta','Administrador']))

def registrar_proyecto(request):
    error = None

    if request.method == 'POST':
        nombre = request.POST.get('txtNombre')
        descripcion = request.POST.get('txtDescripcion')
        fecha_inicio_str = request.POST.get('txtFechaInicio')
        fecha_fin_str = request.POST.get('txtFechaFin')
        estado_form = request.POST.get('estado')
        imagen = request.FILES.get('txtImagen')
        
        if not (nombre and descripcion and fecha_inicio_str):
            error = "Todos los campos son obligatorios"
        else:
            fecha_inicio = date.fromisoformat(fecha_inicio_str)
            fecha_fin = date.fromisoformat(fecha_fin_str) if fecha_fin_str else None

            hoy = date.today()

            if estado_form == 'cancelado':
                estado_final = 'cancelado'
            elif estado_form == 'realizado':
                estado_final = 'realizado'
            else:
                estado_final = 'en_curso' if not fecha_fin or fecha_fin > hoy else 'realizado'

            if not error:

                Proyecto.objects.create(
                    nombre=nombre,
                    descripcion=descripcion,
                    fecha_inicio=fecha_inicio,
                    fecha_fin=fecha_fin,
                    estado=estado_final,
                    imagen=imagen
                )

            return redirect('tabla_proyectos')
    proyectos = Proyecto.objects.all().order_by('-fecha_inicio') 
    return render(request, 'proyectos/tabla_proyectos.html', {'proyectos': proyectos,'error': error})

@login_required
@user_passes_test(roles_permitidos(['Secretaria', 'Presidenta','Administrador']))

def editar_proyecto(request, proyecto_id):
    proyecto = Proyecto.objects.get(id=proyecto_id)
    error = None

    if request.method == 'POST':
        proyecto.nombre = request.POST.get('txtNombre')
        proyecto.descripcion = request.POST.get('txtDescripcion')
        proyecto.fecha_inicio = date.fromisoformat(request.POST.get('txtFechaInicio'))
        fecha_fin_str = request.POST.get('txtFechaFin')
        proyecto.fecha_fin = date.fromisoformat(fecha_fin_str) if fecha_fin_str else None
        estado_form = request.POST.get('estado')

        hoy = date.today()
        if estado_form == 'realizado' and not proyecto.fecha_fin:
            error = "Para marcar un proyecto como realizado, debes definir la fecha fin"
        elif estado_form == 'en_curso' and proyecto.fecha_fin and proyecto.fecha_fin < hoy:
            error = "No puedes marcar como en curso un proyecto cuya fecha ya pasó."
        elif estado_form == 'realizado' and proyecto.fecha_fin and proyecto.fecha_fin > hoy:
            error = "No puedes marcar como realizado un proyecto con fecha futura."

        else:
            proyecto.estado = estado_form

            if request.FILES.get('txtImagen'):
                proyecto.imagen = request.FILES.get('txtImagen')

            proyecto.save()
            return redirect('tabla_proyectos')

    return render(request, 'proyectos/editar_proyecto.html', {'proyecto': proyecto, 'error': error})

@login_required
@user_passes_test(roles_permitidos(['Secretaria', 'Presidenta','Administrador']))

def eliminar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id) 
    proyecto.delete()  
    
    return redirect('tabla_proyectos')


@login_required
@user_passes_test(roles_permitidos(['Secretaria', 'Presidenta','Administrador']))

def agregar_imagen_galeria(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)

    if request.method == "POST":
        imagenes = request.FILES.getlist("imagenes")  

        for img in imagenes:
            ImagenProyecto.objects.create(
                proyecto=proyecto,
                imagen_galeria=img,
            )

        return redirect("editar_proyecto", proyecto_id=proyecto_id)

    return render(request, "proyectos/tabla_proyectos.html", {"proyecto": proyecto})

@login_required
@user_passes_test(roles_permitidos(['Secretaria', 'Presidenta','Administrador']))

def eliminar_imagen_galeria(request, imagen_id):
    imagen = get_object_or_404(ImagenProyecto, id=imagen_id)
    proyecto_id = imagen.proyecto.id
    imagen.delete()
    return redirect("editar_proyecto", proyecto_id=proyecto_id)
