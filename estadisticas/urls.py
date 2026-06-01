from django.urls import path

from .views import EstadisticaDashboardView
from .pdf import generar_reporte_pdf

urlpatterns = [
    path('', EstadisticaDashboardView.as_view(), name='estadisticas_dashboard'),
    path('reporte-pdf/', generar_reporte_pdf, name='reporte_pdf'),
]
