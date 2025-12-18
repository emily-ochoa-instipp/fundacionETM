from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import DocumentoTransparenciaForm
from .models import DocumentoTransparencia

@login_required
def tabla_transparencia(request):
    documentos = DocumentoTransparencia.objects.all()
    form = DocumentoTransparenciaForm()
    return render(request, 'transparencia/tabla_transparencia.html', {
        'documentos': documentos, 'form': form
    })

@login_required
def crear_documento(request):
    if request.method == 'POST':
        form = DocumentoTransparenciaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tabla_transparencia')
    else:
        form = DocumentoTransparenciaForm()

    return render(request, 'transparencia/tabla_transparencia.html', {
        'form': form
    })

@login_required
def editar_documento(request, id):
    documento = get_object_or_404(DocumentoTransparencia, id=id)

    if request.method == 'POST':
        form = DocumentoTransparenciaForm(
            request.POST,
            request.FILES,
            instance=documento
        )
        if form.is_valid():
            form.save()
            return redirect('tabla_transparencia')
    else:
        form = DocumentoTransparenciaForm(instance=documento)

    return render(request, 'transparencia/editar_documento.html', {
        'form': form,
        'editar': True
    })

@login_required
def eliminar_documento(request, id):
    documento = get_object_or_404(DocumentoTransparencia, id=id)

    if request.method == 'POST':
        documento.delete()
        return redirect('tabla_transparencia')

    return render(request, 'transparencia/eliminar_documento.html', {
        'documento': documento
    })
