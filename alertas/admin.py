from django.contrib import admin

from .models import Alerta

@admin.register(Alerta)
class AlertaAdmin(admin.ModelAdmin):
    list_display = ['incidente', 'mensaje', 'fecha', 'leido', 'creado_por']
    list_filter = ['leido', 'fecha']
    search_fields = ['mensaje', 'incidente__titulo', 'creado_por__username']
