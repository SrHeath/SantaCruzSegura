from django.db import models

class EstadisticaIncidente(models.Model):
    nombre = models.CharField(max_length=100)
    valor = models.FloatField()
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Estadística de Incidente'
        verbose_name_plural = 'Estadísticas de Incidentes'

    def __str__(self):
        return f"{self.nombre}: {self.valor}"
