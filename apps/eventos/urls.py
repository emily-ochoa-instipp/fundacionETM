from django.urls import path
from . import views

urlpatterns = [
    # Vistas de eventos

    path('listar_eventos/', views.tabla_eventos, name='tabla_eventos'),
    path('eventos/registrar/', views.registrar_evento, name='registrar_evento'),
    path('eventos/editar/<int:evento_id>/', views.editar_evento, name='editar_evento'),
    path('eventos/eliminar/<int:evento_id>/', views.eliminar_evento, name='eliminar_evento'),
]
