import mimetypes
import os

from django.conf import settings
from django.contrib import admin
from django.http import FileResponse, Http404
from django.urls import include, path, re_path

def media_serve(request, path):
    file_path = os.path.normpath(os.path.join(settings.MEDIA_ROOT, path))
    media_root = os.path.normpath(str(settings.MEDIA_ROOT))
    if not os.path.exists(file_path) or not file_path.startswith(media_root + os.sep):
        raise Http404
    content_type, _ = mimetypes.guess_type(file_path)
    return FileResponse(open(file_path, 'rb'), content_type=content_type or 'application/octet-stream')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),
    path('incidentes/', include('incidentes.urls')),
    path('estadisticas/', include('estadisticas.urls')),
    path('predicciones/', include('predicciones.urls')),
    path('alertas/', include('alertas.urls')),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', media_serve),
]
