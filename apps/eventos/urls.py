from django.urls import path
from . import views

urlpatterns = [
    # Vistas de eventos

    path('listar_eventos/', views.tabla_eventos, name='tabla_eventos'),
    path('eventos/registrar/', views.registrar_evento, name='registrar_evento'),
    path('eventos/editar/<int:evento_id>/', views.editar_evento, name='editar_evento'),
    path('eventos/eliminar/<int:evento_id>/', views.eliminar_evento, name='eliminar_evento'),

    path('evento/<int:evento_id>/agregar-imagen/', views.agregar_imagen_galeria, name='agregar_imagen_galeria'),
    path('imagen/<int:imagen_id>/eliminar/', views.eliminar_imagen_galeria, name='eliminar_imagen_galeria'),
]

