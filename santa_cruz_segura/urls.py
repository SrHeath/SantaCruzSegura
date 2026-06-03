from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),
    path('incidentes/', include('incidentes.urls')),
    path('estadisticas/', include('estadisticas.urls')),
    path('predicciones/', include('predicciones.urls')),
    path('alertas/', include('alertas.urls')),
]
