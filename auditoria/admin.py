from django.contrib import admin

from .models import AuditLog

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'usuario', 'accion', 'modelo', 'registro_id']
    list_filter = ['modelo', 'accion', 'fecha']
    search_fields = ['usuario__username', 'accion', 'modelo', 'detalles']
