from django.db import models

from incidentes.models import Incidente
from usuarios.models import Usuario

class Alerta(models.Model):
    incidente = models.ForeignKey(Incidente, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=250)
    fecha = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)
    creado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Alerta'
        verbose_name_plural = 'Alertas'
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.fecha} - {self.mensaje[:50]}"

class SuscripcionAlerta(models.Model):
    CANAL_CHOICES = [
        ('whatsapp', 'WhatsApp'),
        ('telegram', 'Telegram'),
        ('ambos', 'Ambos'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='suscripciones_alertas')
    sector = models.ForeignKey('incidentes.Sector', on_delete=models.CASCADE)
    canal_preferido = models.CharField(max_length=20, choices=CANAL_CHOICES, default='ambos')
    recibir_predictivas = models.BooleanField(default=True)
    fecha_suscripcion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Suscripción a Alertas'
        verbose_name_plural = 'Suscripciones a Alertas'
        unique_together = ('usuario', 'sector')

    def __str__(self):
        return f"{self.usuario.username} suscrito a {self.sector.nombre}"

