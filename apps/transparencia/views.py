from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from apps.usuarios.decorators import roles_permitidos
from .models import CategoriaDocumento, DocumentoTransparencia


@login_required
@user_passes_test(roles_permitidos(['Secretaria', 'Presidenta']))

def tabla_documentos(request):
    documentos = DocumentoTransparencia.objects.all()
    categorias = CategoriaDocumento.objects.filter(estado=True)
    return render(request, 'transparencia/tabla_documentos.html', {
        'documentos': documentos, 'categorias': categorias 
    })


@login_required
@user_passes_test(roles_permitidos(['Secretaria', 'Presidenta']))

def crear_documento(request):
    if request.method == 'POST':
        nombre = request.POST.get('txtNombre')
        archivo = request.FILES.get('archivo')
        categoria_id = request.POST.get('categoria')
        estado = True if request.POST.get('estado') else False

        categoria = get_object_or_404(CategoriaDocumento, id=categoria_id)

        DocumentoTransparencia.objects.create(
            nombre=nombre,
            archivo=archivo,
            categoria=categoria,
            estado=estado
        )

        messages.success(request, 'Documento agregado correctamente.')
        return redirect('tabla_documentos')

    return redirect('tabla_documentos')

@login_required
@user_passes_test(roles_permitidos(['Secretaria', 'Presidenta']))

def editar_documento(request, id):
    documento = get_object_or_404(DocumentoTransparencia, id=id)
    categorias = CategoriaDocumento.objects.filter(estado=True)

    if request.method == 'POST':
        documento.nombre = request.POST.get('txtNombre')
        documento.estado = True if request.POST.get('estado') else False

        categoria_id = request.POST.get('categoria')
        documento.categoria = get_object_or_404(CategoriaDocumento, id=categoria_id)

        if 'archivo' in request.FILES:
            documento.archivo = request.FILES['archivo']

        documento.save()
        messages.success(request, 'Documento actualizado.')
        return redirect('tabla_documentos')

    return render(request, 'transparencia/editar_documento.html', {
        'documento': documento,
        'categorias': categorias
    })

@login_required
@user_passes_test(roles_permitidos(['Secretaria', 'Presidenta']))

def eliminar_documento(request, id):
    documento = get_object_or_404(DocumentoTransparencia, id=id)

    documento.delete()
    messages.success(request, 'Documento eliminado correctamente.')
    return redirect('tabla_documentos')


@login_required
@user_passes_test(roles_permitidos(['Secretaria', 'Presidenta']))

def tabla_categorias(request):
    categorias = CategoriaDocumento.objects.all()
    return render(request, 'transparencia/tabla_categorias.html', {
        'categorias': categorias
    })

@login_required
@user_passes_test(roles_permitidos(['Secretaria', 'Presidenta']))

def crear_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('txtNombre')
        estado = True if request.POST.get('estado') else False

        CategoriaDocumento.objects.create(
            nombre=nombre,
            estado=estado
        )

        messages.success(request, 'Categoría creada correctamente.')
        return redirect('tabla_categorias')

    return redirect('tabla_categorias')

@login_required
@user_passes_test(roles_permitidos(['Secretaria', 'Presidenta']))

def editar_categoria(request, id):
    categoria = get_object_or_404(CategoriaDocumento, id=id)

    if request.method == 'POST':
        categoria.nombre = request.POST.get('txtNombre')
        categoria.estado = True if request.POST.get('estado') else False
        categoria.save()

        messages.success(request, 'Categoría actualizada.')
        return redirect('tabla_categorias')

    return render(request, 'transparencia/editar_categoria.html', {
        'categoria': categoria
    })

@login_required
@user_passes_test(roles_permitidos(['Secretaria', 'Presidenta']))

def eliminar_categoria(request, id):
    categoria = get_object_or_404(CategoriaDocumento, id=id)
    categoria.delete()
    messages.success(request, 'Categoría eliminada.')
    return redirect('tabla_categorias')
