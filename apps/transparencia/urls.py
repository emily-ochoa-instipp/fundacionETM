from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.tabla_categorias, name='tabla_categorias'),
    path('categorias/crear/', views.crear_categoria, name='crear_categoria'),
    path('transparencia/categorias/editar/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('transparencia/categorias/eliminar/<int:id>/', views.eliminar_categoria, name='eliminar_categoria'),

    path('documentos/', views.tabla_documentos, name='tabla_documentos'),
    path('documentos/crear/', views.crear_documento, name='crear_documento'),
    path('documentos/editar/<int:id>/', views.editar_documento, name='editar_documento'),
    path('documentos/eliminar/<int:id>/', views.eliminar_documento, name='eliminar_documento'),
]
