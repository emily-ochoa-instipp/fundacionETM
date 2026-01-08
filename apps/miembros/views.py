from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Case, When, Value, IntegerField
from .models import Miembro
from apps.usuarios.decorators import roles_permitidos


@login_required
@user_passes_test(roles_permitidos(['Secretaria', 'Presidenta','Administrador']))

def tabla_miembros(request):
    miembros = Miembro.objects.annotate(
        orden=Case(
            When(cargo='presidenta', then=Value(1)),
            When(cargo='secretaria', then=Value(2)),
            When(cargo='tesorera', then=Value(3)),
            When(cargo='socia', then=Value(4)),
            default=Value(5),
            output_field=IntegerField(),
        )
    ).order_by('orden', 'apellido')

    return render(request, 'miembros/tabla_miembros.html', {
        'miembros': miembros, 'cargos': Miembro.CARGO_CHOICES
    })


@login_required
@user_passes_test(roles_permitidos(['Secretaria', 'Presidenta','Administrador']))

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
@user_passes_test(roles_permitidos(['Secretaria', 'Presidenta','Administrador']))

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
@user_passes_test(roles_permitidos(['Secretaria', 'Presidenta','Administrador']))

def eliminar_miembro(request, id):
    miembro = get_object_or_404(Miembro, id=id)
    miembro.delete()
    messages.success(request, 'Miembro eliminado correctamente.')
    return redirect('tabla_miembros')
