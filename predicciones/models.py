from django.db import models

from incidentes.models import Sector, TipoDelito

class PrediccionZona(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoDelito, on_delete=models.CASCADE)
    probabilidad = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Predicción de Zona'
        verbose_name_plural = 'Predicciones de Zonas'
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.sector} - {self.tipo} ({self.probabilidad:.2f})"

class ModeloIA(models.Model):
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('descartado', 'Descartado'),
    ]
    version = models.CharField(max_length=50)
    fecha_entrenamiento = models.DateTimeField(auto_now_add=True)
    precision_obtenida = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    registros_usados = models.IntegerField(default=0)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='activo')
    ruta_archivo = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Modelo IA'
        verbose_name_plural = 'Modelos IA'

    def __str__(self):
        return f"Modelo v{self.version} ({self.estado}) - {self.precision_obtenida}%"

