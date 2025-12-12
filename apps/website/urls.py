from django.urls import path
from . import views

urlpatterns = [
    # Vistas de website
    path('', views.index_views, name='index'),

    # path('nosotras/', views.nosotras, name='nosotras'),
    path('eventos/', views.eventos_views, name='eventos'),
    path('proyectos/', views.proyectos_views, name='proyectos'),
    path('evento/<int:id>/', views.evento_detalles, name='evento_detalles'),
    path('proyecto/<int:id>/', views.proyecto_detalles, name='proyecto_detalles'),
    # path('nosotras/', views.nosotras, name='nosotras'),
    # path('nosotras/', views.nosotras, name='nosotras'),
    
]
