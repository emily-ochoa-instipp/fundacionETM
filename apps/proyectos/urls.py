from django.urls import path
from . import views

urlpatterns = [
    # Vistas de proyectos

    path('listar_proyectos/', views.tabla_proyectos, name='tabla_proyectos'),
    path('proyectos/registrar/', views.registrar_proyecto, name='registrar_proyecto'),
    path('proyectos/editar/<int:proyecto_id>/', views.editar_proyecto, name='editar_proyecto'),
    path('proyectos/eliminar/<int:proyecto_id>/', views.eliminar_proyecto, name='eliminar_proyecto'),


    # path('evento/<int:evento_id>/agregar-imagen/', views.agregar_imagen_galeria, name='agregar_imagen_galeria'),
    # path('imagen/<int:imagen_id>/eliminar/', views.eliminar_imagen_galeria, name='eliminar_imagen_galeria'),
]

