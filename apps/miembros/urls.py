from django.urls import path
from . import views

urlpatterns = [
    path('miembros/', views.tabla_miembros, name='tabla_miembros'),
    path('miembros/crear/', views.registrar_miembro, name='registrar_miembro'),
    path('miembros/editar/<int:id>/', views.editar_miembro, name='editar_miembro'),
    path('miembros/eliminar/<int:id>/', views.eliminar_miembro, name='eliminar_miembro'),
]
