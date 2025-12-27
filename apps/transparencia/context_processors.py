from .models import CategoriaDocumento

def menu_transparencia(request):
    categorias = CategoriaDocumento.objects.filter(
        estado=True,
        documentos__estado=True
    ).distinct()

    return {
        'menu_categorias': categorias
    }
