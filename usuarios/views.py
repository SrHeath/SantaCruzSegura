from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView, UpdateView
from django.core.cache import cache
from django.http import HttpResponseForbidden

from .forms import UsuarioRegistroForm, UsuarioActualizarForm, UsuarioRegistroPublicoForm
from .models import Usuario

class LoginUsuario(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        cache_key = f'login_attempts_{self.request.META.get("REMOTE_ADDR", "unknown")}'
        cache.delete(cache_key)
        return super().form_valid(form)

    def form_invalid(self, form):
        ip = self.request.META.get("REMOTE_ADDR", "unknown")
        cache_key = f'login_attempts_{ip}'
        attempts = cache.get(cache_key, 0)
        cache.set(cache_key, attempts + 1, 300)
        if attempts >= 5:
            return HttpResponseForbidden("Demasiados intentos de login. Espera 5 minutos.")
        return super().form_invalid(form)

class RegistroUsuario(CreateView):
    form_class = UsuarioRegistroPublicoForm
    template_name = 'registro.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        response = super().form_valid(form)
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
        rol = getattr(self.request.user, 'rol', None)
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