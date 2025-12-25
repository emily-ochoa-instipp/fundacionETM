from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import MujerReferente


@login_required
def tabla_mujeres_referentes(request):
    mujeres = MujerReferente.objects.all()
    return render(request, 'mujeres_referentes/tabla_mujeres_referentes.html', {
        'mujeres': mujeres
    })

@login_required
def registrar_mujer_referente(request):
    if request.method == 'POST':
        nombre_ = request.POST.get('txtNombre')
        lugar_origen_ = request.POST.get('txtLugarOrigen')
        ocupacion_ = request.POST.get('txtOcupacion')
        descripcion_ = request.POST.get('txtDescripcion')
        imagen_ = request.FILES.get('imagen')
        estado_ = True if request.POST.get('estado') else False

        MujerReferente.objects.create(
            nombre=nombre_,
            lugar_origen=lugar_origen_,
            ocupacion=ocupacion_,
            descripcion=descripcion_,
            imagen=imagen_,
            estado=estado_
        )

        messages.success(request, 'Mujer referente registrada correctamente.')
        return redirect('tabla_mujeres_referentes')

    return render(request, 'mujeres_referentes/tabla_mujeres_referentes.html')

@login_required
def editar_mujer_referente(request, id):
    mujer = get_object_or_404(MujerReferente, id=id)

    if request.method == 'POST':
        mujer.nombre = request.POST.get('txtNombre')
        mujer.lugar_origen = request.POST.get('txtLugarOrigen')
        mujer.ocupacion = request.POST.get('txtOcupacion')
        mujer.descripcion = request.POST.get('txtDescripcion')
        mujer.estado = True if request.POST.get('estado') else False

        if 'imagen' in request.FILES:
            mujer.imagen = request.FILES['imagen']

        mujer.save()
        messages.success(request, 'Datos actualizados correctamente.')
        return redirect('tabla_mujeres_referentes')

    return render(request, 'mujeres_referentes/editar_mujer_referente.html', {
        'mujer': mujer
    })

@login_required
def eliminar_mujer_referente(request, id):
    mujer = get_object_or_404(MujerReferente, id=id)
    mujer.delete()
    messages.success(request, 'Registro eliminado correctamente.')
    return redirect('tabla_mujeres_referentes')
