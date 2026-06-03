from django.urls import path

from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('login/', views.LoginUsuario.as_view(), name='login'),
    path('registro/', views.RegistroUsuario.as_view(), name='registro'),
    path('logout/', views.LogoutUsuario.as_view(), name='logout'),
    path('usuarios/', views.UsuarioListView.as_view(), name='usuario_lista'),
    path('usuarios/crear/', views.UsuarioCrearView.as_view(), name='usuario_crear'),
    path('usuarios/<int:pk>/rol/', views.UsuarioRolUpdateView.as_view(), name='usuario_rol'),
    path('perfil/', views.PerfilView.as_view(), name='perfil'),
]
