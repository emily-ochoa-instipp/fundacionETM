from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Miembro


@login_required
def tabla_miembros(request):
    miembros = Miembro.objects.all()
    return render(request, 'miembros/tabla_miembros.html', {
        'miembros': miembros, 'cargos': Miembro.CARGO_CHOICES
    })


@login_required
def registrar_miembro(request):
    if request.method == 'POST':
        nombre_ = request.POST.get('txtNombre')
        apellido_ = request.POST.get('txtApellido')
        descripcion_ = request.POST.get('txtDescripcion')
        cargo_ = request.POST.get('cargo')
        foto_ = request.FILES.get('foto')
        estado_ = True if request.POST.get('estado') else False

        Miembro.objects.create(
            nombre=nombre_,
            apellido=apellido_,
            descripcion=descripcion_,
            cargo=cargo_,
            foto=foto_,
            estado=estado_
        )

        messages.success(request, 'Miembro registrado correctamente.')
        return redirect('tabla_miembros')

    return render(request, 'miembros/tabla_miembros.html')


@login_required
def editar_miembro(request, id):
    miembro = get_object_or_404(Miembro, id=id)

    if request.method == 'POST':
        miembro.nombre = request.POST.get('txtNombre')
        miembro.apellido = request.POST.get('txtApellido')
        miembro.descripcion = request.POST.get('txtDescripcion')
        miembro.cargo = request.POST.get('cargo')
        miembro.estado = True if request.POST.get('estado') else False

        if 'foto' in request.FILES:
            miembro.foto = request.FILES['foto']

        miembro.save()
        messages.success(request, 'Datos actualizados correctamente.')
        return redirect('tabla_miembros')

    return render(request, 'miembros/editar_miembro.html', {
        'miembro': miembro
    })


@login_required
def eliminar_miembro(request, id):
    miembro = get_object_or_404(Miembro, id=id)
    miembro.delete()
    messages.success(request, 'Miembro eliminado correctamente.')
    return redirect('tabla_miembros')
