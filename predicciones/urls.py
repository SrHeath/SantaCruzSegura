from django.urls import path

from .views import PrediccionListView, MapaCalorAPIView

urlpatterns = [
    path('', PrediccionListView.as_view(), name='prediccion_lista'),
    path('api/mapa-calor/', MapaCalorAPIView.as_view(), name='mapa_calor_api'),
]
