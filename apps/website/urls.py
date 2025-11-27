from django.urls import path
from . import views

urlpatterns = [
    # Vistas de website
    path('', views.index_views, name='index'),

    # path('nosotras/', views.nosotras, name='nosotras'),
    path('website/', views.eventos_views, name='eventos'),
    path('eventos/<int:id>/', views.evento_detalles, name='evento_detalles'),
    # path('nosotras/', views.nosotras, name='nosotras'),
    # path('nosotras/', views.nosotras, name='nosotras'),
    
]
