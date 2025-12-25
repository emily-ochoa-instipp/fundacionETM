from django.urls import path
from . import views

urlpatterns = [
    path('mujeres_referentes/', views.tabla_mujeres_referentes, name='tabla_mujeres_referentes'),
    path('mujeres_referentes/crear/', views.registrar_mujer_referente, name='registrar_mujer_referente'),
    path('mujeres_referentes/editar/<int:id>/', views.editar_mujer_referente, name='editar_mujer_referente'),
    path('mujeres_referentes/eliminar/<int:id>/', views.eliminar_mujer_referente, name='eliminar_mujer_referente'),
]
