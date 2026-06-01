from django.contrib import admin

from .models import Incidente, Sector, TipoDelito

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']

@admin.register(TipoDelito)
class TipoDelitoAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']

@admin.register(Incidente)
class IncidenteAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'sector', 'tipo', 'reporte_por', 'fecha_hora', 'activo']
    list_filter = ['sector', 'tipo', 'activo']
    search_fields = ['titulo', 'descripcion', 'direccion']
    readonly_fields = ['fecha_hora']
