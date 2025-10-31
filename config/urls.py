
from django.contrib import admin
from django.urls import include, path
from apps.autenticacion import views as autenticacion_views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', autenticacion_views.login_view, name='login'),
    path('autenticacion/', include('apps.autenticacion.urls')),
    path('dashboard/', include('apps.dashboard.urls')),
    path('inicio/', include('apps.inicio.urls')),
    # path('pagos/', include('apps.pagos.urls')),
    # path('reportes/', include('apps.reportes.urls')),
    path('usuarios/', include('apps.usuarios.urls')),
    path('proyectos/', include('apps.proyectos.urls')),
    path('eventos/', include('apps.eventos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
