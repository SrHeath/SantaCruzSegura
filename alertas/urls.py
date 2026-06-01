from django.urls import path

from . import views

urlpatterns = [
    path('', views.AlertaListView.as_view(), name='alerta_lista'),
    path('configurar/', views.SuscripcionAlertaConfigView.as_view(), name='alerta_suscripcion_config'),
]
