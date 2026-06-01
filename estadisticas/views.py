from django.db.models import Count
from django.shortcuts import render
from django.views import View

from incidentes.models import Incidente

class EstadisticaDashboardView(View):
    def get(self, request):
        incidentes_por_tipo = Incidente.objects.values('tipo__nombre').annotate(total=Count('id')).order_by('-total')
        incidentes_por_sector = Incidente.objects.values('sector__nombre').annotate(total=Count('id')).order_by('-total')
        context = {
            'incidentes_por_tipo': incidentes_por_tipo,
            'incidentes_por_sector': incidentes_por_sector,
        }
        return render(request, 'estadisticas/dashboard.html', context)
