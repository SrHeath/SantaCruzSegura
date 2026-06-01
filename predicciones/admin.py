from django.contrib import admin

from .models import PrediccionZona

@admin.register(PrediccionZona)
class PrediccionZonaAdmin(admin.ModelAdmin):
    list_display = ['sector', 'tipo', 'probabilidad', 'fecha']
    list_filter = ['fecha', 'sector', 'tipo']
    search_fields = ['sector__nombre', 'tipo__nombre']
