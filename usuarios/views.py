from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView, TemplateView, UpdateView
from django.http import HttpResponse
from datetime import timedelta

from auditoria.models import AuditLog
from auditoria.middleware import get_client_ip
from .forms import UsuarioRegistroForm, UsuarioActualizarForm, UsuarioRegistroPublicoForm
from .models import Usuario

MAX_LOGIN_ATTEMPTS_IP = 10
LOGIN_BLOCK_MINUTES = 15


class LoginUsuario(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def dispatch(self, request, *args, **kwargs):
        ip = get_client_ip(request)
        cutoff = timezone.now() - timedelta(minutes=LOGIN_BLOCK_MINUTES)
        recent = AuditLog.objects.filter(
            ip_origen=ip,
            accion__in=['Login fallido', 'Intento login invalido'],
            fecha__gte=cutoff
        ).count()
        if recent >= MAX_LOGIN_ATTEMPTS_IP:
            response = HttpResponse(
                f"Demasiados intentos de login desde esta IP. Espera {LOGIN_BLOCK_MINUTES} minutos.",
                status=429,
            )
            response['Retry-After'] = str(LOGIN_BLOCK_MINUTES * 60)
            return response
        return super().dispatch(request, *args, **kwargs)


class RegistroUsuario(CreateView):
    form_class = UsuarioRegistroPublicoForm
    template_name = 'registro.html'
    success_url = reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        if not getattr(settings, 'REGISTRATION_OPEN', False):
            messages.error(request, "El registro publico esta deshabilitado.")
            return redirect('login')
        ip = get_client_ip(request)
        cutoff = timezone.now() - timedelta(hours=1)
        registros_recientes = AuditLog.objects.filter(
            ip_origen=ip,
            accion='Registro de usuario',
            fecha__gte=cutoff
        ).count()
        if registros_recientes >= 3:
            response = HttpResponse(
                "Has excedido el limite de registros. Intenta mas tarde.",
                status=429,
            )
            response['Retry-After'] = '3600'
            return response
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        ip = get_client_ip(self.request)
        AuditLog.objects.create(
            usuario=self.object,
            accion='Registro de usuario',
            modelo='Usuario',
            registro_id=self.object.pk,
            detalles=f'Nuevo usuario registrado: {self.object.username}',
            ip_origen=ip,
        )
        return redirect('login')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().get(request, *args, **kwargs)


class LogoutUsuario(LogoutView):
    next_page = reverse_lazy('login')


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
    login_url = 'login'

class UsuarioListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Usuario
    template_name = 'usuarios/lista.html'
    context_object_name = 'usuarios'

    def test_func(self):
        if not self.request.user.is_authenticated:
            return False
        user = self.request.user
        if user.is_superuser:
            return True
        rol = getattr(user, 'rol', None)
        return rol and rol.nombre in ['Superadministrador', 'Administrador de Junta']

class UsuarioCrearView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Usuario
    form_class = UsuarioRegistroForm
    template_name = 'usuarios/crear.html'
    success_url = reverse_lazy('usuario_lista')

    def test_func(self):
        if not self.request.user.is_authenticated:
            return False
        rol = getattr(self.request.user, 'rol', None)
        return rol and rol.nombre == 'Superadministrador'

class PerfilView(LoginRequiredMixin, UpdateView):
    model = Usuario
    form_class = UsuarioActualizarForm
    template_name = 'usuarios/perfil.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        return self.request.user


class UsuarioRolUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Usuario
    fields = ['rol', 'estado', 'barrio']
    template_name = 'usuarios/cambiar_rol.html'
    success_url = reverse_lazy('usuario_lista')

    def test_func(self):
        if not self.request.user.is_authenticated:
            return False
        user = self.request.user
        if user.is_superuser:
            return True
        rol = getattr(user, 'rol', None)
        if not rol:
            return False
        if rol.nombre == 'Superadministrador':
            return True
        if rol.nombre == 'Administrador de Junta':
            target = self.get_object()
            return user.barrio and target.barrio == user.barrio
        return False

    def form_valid(self, form):
        old_rol = getattr(self.object.rol, 'nombre', 'Sin rol')
        response = super().form_valid(form)
        new_rol = getattr(self.object.rol, 'nombre', 'Sin rol')
        AuditLog.objects.create(
            usuario=self.request.user,
            accion='Cambio de rol',
            modelo='Usuario',
            registro_id=self.object.pk,
            detalles=f'Rol cambiado de "{old_rol}" a "{new_rol}", Estado: {self.object.estado}',
            ip_origen=get_client_ip(self.request),
        )
        messages.success(self.request, f'Rol de {self.object.username} actualizado.')
        return response