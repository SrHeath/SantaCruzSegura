from django.db.models.signals import post_save
from django.dispatch import receiver

from incidentes.models import Incidente
from .models import AuditLog
from .middleware import get_client_ip

@receiver(post_save, sender=Incidente)
def registrar_incidente(sender, instance, created, **kwargs):
    accion = 'Creado' if created else 'Actualizado'
    AuditLog.objects.create(
        usuario=instance.reporte_por,
        accion=f'{accion} incidente',
        modelo='Incidente',
        registro_id=instance.pk,
        detalles=instance.titulo,
        ip_origen=get_client_ip(),
    )

