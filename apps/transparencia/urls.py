from django.urls import path
from . import views

urlpatterns = [
    path('transparencia/', views.tabla_transparencia, name='tabla_transparencia'),
    path('transparencia/crear/', views.crear_documento, name='crear_documento'),
    path('transparencia/editar/<int:id>/', views.editar_documento, name='editar_documento'),
    path('transparencia/eliminar/<int:id>/', views.eliminar_documento, name='eliminar_documento'),
]
