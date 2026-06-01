from django.db import models
from usuarios.models import Usuario

class Sector(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    centro_lat = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    centro_lon = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)

    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectores'

    def __str__(self):
        return self.nombre

class TipoDelito(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Tipo de Delito'
        verbose_name_plural = 'Tipos de Delito'

    def __str__(self):
        return self.nombre

class Incidente(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('validado', 'Validado'),
        ('falso', 'Falso'),
    ]

    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    latitud = models.DecimalField(max_digits=10, decimal_places=7)
    longitud = models.DecimalField(max_digits=10, decimal_places=7)
    direccion = models.CharField(max_length=255)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoDelito, on_delete=models.CASCADE)
    reporte_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='incidentes_reportados')
    imagen = models.ImageField(upload_to='incidentes/', blank=True, null=True)
    activo = models.BooleanField(default=True)

    # Nuevos campos del flujo de validación y consignas
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    validador = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='incidentes_validados')
    fecha_hora_validacion = models.DateTimeField(null=True, blank=True)
    num_testigos = models.IntegerField(default=1)
    reporte_anonimo = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Incidente'
        verbose_name_plural = 'Incidentes'
        ordering = ['-fecha_hora']

    def __str__(self):
        return f"{self.titulo} - {self.sector}"


class Testigo(models.Model):
    CANAL_CHOICES = [
        ('web', 'Web'),
        ('whatsapp', 'WhatsApp'),
        ('voz', 'Voz'),
        ('telegram', 'Telegram'),
    ]

    incidente = models.ForeignKey(Incidente, on_delete=models.CASCADE, related_name='testigos')
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    canal_origen = models.CharField(max_length=20, choices=CANAL_CHOICES, default='web')
    fecha_reporte = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='testigos/', blank=True, null=True)
    reporte_anonimo = models.BooleanField(default=False)



    class Meta:
        verbose_name = 'Testigo'
        verbose_name_plural = 'Testigos'

    def __str__(self):
        return f"Testigo {self.pk} del incidente {self.incidente.pk}"


class OperativoPolicial(models.Model):
    policia = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_inicio = models.TimeField(null=True, blank=True)
    hora_fin = models.TimeField(null=True, blank=True)
    num_agents = models.IntegerField(default=1)
    zona_asignada = models.CharField(max_length=200, blank=True)
    notas = models.TextField(blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Operativo Policial'
        verbose_name_plural = 'Operativos Policiales'

    def __str__(self):
        return f"Operativo {self.pk} en {self.sector} el {self.fecha}"

