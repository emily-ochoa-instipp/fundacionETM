from django.urls import path
from . import views

urlpatterns = [
    # Vistas de website
    path('', views.index_views, name='index'),

    # path('nosotras/', views.nosotras, name='nosotras'),
    path('website/', views.eventos_views, name='eventos'),
    # path('nosotras/', views.nosotras, name='nosotras'),
    # path('nosotras/', views.nosotras, name='nosotras'),
    # path('nosotras/', views.nosotras, name='nosotras'),
    
]
