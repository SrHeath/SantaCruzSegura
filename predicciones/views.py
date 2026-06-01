from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from .ml import predecir_riesgo
from .models import PrediccionZona
from incidentes.models import Sector, TipoDelito, Incidente


class PrediccionListView(LoginRequiredMixin, View):
    def get(self, request):
        predicciones = PrediccionZona.objects.order_by('-fecha')[:20]
        sectores = Sector.objects.all()
        tipos = TipoDelito.objects.all()
        return render(request, 'predicciones/lista.html', {
            'predicciones': predicciones,
            'sectores': sectores,
            'tipos': tipos
        })

    def post(self, request):
        lat = float(request.POST.get('latitud') or 0)
        lng = float(request.POST.get('longitud') or 0)
        sector_id = int(request.POST.get('sector') or 0)
        tipo_id = int(request.POST.get('tipo') or 0)
        
        if sector_id and tipo_id:
            prob = predecir_riesgo(lat, lng, sector_id, tipo_id)
            prediccion = PrediccionZona.objects.create(
                sector_id=sector_id,
                tipo_id=tipo_id,
                probabilidad=prob,
            )
        
        predicciones = PrediccionZona.objects.order_by('-fecha')[:20]
        sectores = Sector.objects.all()
        tipos = TipoDelito.objects.all()
        
        return render(request, 'predicciones/lista.html', {
            'predicciones': predicciones,
            'sectores': sectores,
            'tipos': tipos,
            'prediction': prediccion if sector_id and tipo_id else None
        })


class MapaCalorAPIView(LoginRequiredMixin, View):
    def get(self, request):
        """API que retorna datos para el mapa de calor"""
        incidentes = Incidente.objects.filter(activo=True).values(
            'latitud', 'longitud', 'tipo__nombre', 'sector__nombre'
        )
        
        data = {
            'type': 'FeatureCollection',
            'features': []
        }
        
        for inc in incidentes:
            feature = {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [float(inc['longitud']), float(inc['latitud'])]
                },
                'properties': {
                    'tipo': inc['tipo__nombre'],
                    'sector': inc['sector__nombre'],
                    'intensity': 1
                }
            }
            data['features'].append(feature)
        
        return JsonResponse(data)
