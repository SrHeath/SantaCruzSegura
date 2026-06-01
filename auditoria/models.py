from django.db import models

from usuarios.models import Usuario

class AuditLog(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    accion = models.CharField(max_length=200)
    modelo = models.CharField(max_length=100)
    registro_id = models.IntegerField(null=True, blank=True)
    detalles = models.TextField(blank=True)
    ip_origen = models.CharField(max_length=45, blank=True, null=True)


    class Meta:
        verbose_name = 'Registro de Auditoría'
        verbose_name_plural = 'Registros de Auditoría'
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.fecha} - {self.usuario} - {self.accion}"
