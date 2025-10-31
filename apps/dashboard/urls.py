from django.urls import path
from . import views

urlpatterns = [
    # Vistas de dashboard
    path('dashboard_analytics/', views.dashboard_analytics, name='dashboard_analytics'),
    path('dashboard_sales/', views.dashboard_sales, name='dashboard_sales'),
    path('dashboard_saas/', views.dashboard_saas, name='dashboard_saas'),
    path('dashboard_system/', views.dashboard_system, name='dashboard_system'),
]