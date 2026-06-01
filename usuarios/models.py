from django.contrib.auth.models import AbstractUser
from django.db import models

class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.nombre

class Usuario(AbstractUser):
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('inhabilitado', 'Inhabilitado'),
        ('bloqueado', 'Bloqueado'),
    ]

    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True, blank=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='activo')
    intentos_fallidos = models.IntegerField(default=0)
    reportes_falsos_mes = models.IntegerField(default=0)
    barrio = models.ForeignKey('incidentes.Sector', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def save(self, *args, **kwargs):
        self.is_active = (self.estado == 'activo')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.get_full_name() or self.username