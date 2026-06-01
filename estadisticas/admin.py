from django.contrib import admin

from .models import EstadisticaIncidente

@admin.register(EstadisticaIncidente)
class EstadisticaIncidenteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'valor', 'fecha']
    list_filter = ['fecha']
    search_fields = ['nombre']
