from django.urls import path
from . import views

urlpatterns = [
    # Vistas de website
    path('', views.index_views, name='index'),

    path('eventos/', views.eventos_views, name='eventos'),
    path('evento/<int:id>/', views.evento_detalles, name='evento_detalles'),

    path('proyectos/realizados/', views.proyectos_realizados_views, name='proyectos_realizados'),
    path('proyecto/realizado/<int:id>/', views.proyecto_realizado_detalles, name='proyecto_realizado_detalles'),
    path('proyectos/en_curso/', views.proyectos_en_curso_views, name='proyectos_en_curso'),
    path('proyecto/en_curso/<int:id>/', views.proyecto_en_curso_detalles, name='proyecto_en_curso_detalles'),
    
]
