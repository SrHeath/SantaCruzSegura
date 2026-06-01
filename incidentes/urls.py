from django.urls import path

from . import views

urlpatterns = [
    path('', views.IncidenteListView.as_view(), name='incidente_lista'),
    path('crear/', views.IncidenteCrearView.as_view(), name='incidente_crear'),
    path('detalle/<int:pk>/', views.IncidenteDetalleView.as_view(), name='incidente_detalle'),
    path('mapa/', views.IncidenteMapaView.as_view(), name='incidente_mapa'),
    path('bandeja-validacion/', views.IncidenteBandejaValidacionView.as_view(), name='incidente_bandeja_validacion'),
    path('validar/<int:pk>/<str:accion>/', views.IncidenteValidarAccionView.as_view(), name='incidente_validar_accion'),
]
