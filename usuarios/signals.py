from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from django.db.models import F
from .models import Usuario
from auditoria.models import AuditLog
from auditoria.middleware import get_client_ip

@receiver(user_logged_in)
def log_usuario_ingreso(sender, request, user, **kwargs):
    user.intentos_fallidos = 0
    user.save(update_fields=['intentos_fallidos'])
    AuditLog.objects.create(
        usuario=user,
        accion='Login exitoso',
        modelo='Usuario',
        registro_id=user.pk,
        detalles=f'Usuario {user.username} ha iniciado sesión con éxito.',
        ip_origen=get_client_ip(request)
    )

@receiver(user_logged_out)
def log_usuario_salida(sender, request, user, **kwargs):
    if user:
        AuditLog.objects.create(
            usuario=user,
            accion='Cierre de sesión',
            modelo='Usuario',
            registro_id=user.pk,
            detalles=f'Usuario {user.username} ha cerrado sesión.',
            ip_origen=get_client_ip(request)
        )

@receiver(user_login_failed)
def log_usuario_intento_fallido(sender, credentials, request, **kwargs):
    username = credentials.get('username', '')
    ip = get_client_ip(request)
    
    # Intenta buscar al usuario por username o email
    try:
        user = Usuario.objects.get(username=username)
    except Usuario.DoesNotExist:
        try:
            user = Usuario.objects.get(email=username)
        except Usuario.DoesNotExist:
            user = None

    if user:
        user.intentos_fallidos += 1
        detalles = f'Intento fallido {user.intentos_fallidos}/5 para {user.username}.'
        
        if user.intentos_fallidos >= 5:
            user.estado = 'bloqueado'
            detalles += ' La cuenta ha sido BLOQUEADA temporalmente.'
            
        user.save()
        
        AuditLog.objects.create(
            usuario=user,
            accion='Login fallido',
            modelo='Usuario',
            registro_id=user.pk,
            detalles=detalles,
            ip_origen=ip
        )
    else:
        AuditLog.objects.create(
            usuario=None,
            accion='Intento login inválido',
            modelo='Usuario',
            detalles=f'Intento de login con credenciales inexistentes: {username}',
            ip_origen=ip
        )
