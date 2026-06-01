from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Usuario, Rol
from incidentes.models import Sector

class UsuarioRegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido. Ingresa un email válido.')
    first_name = forms.CharField(max_length=30, required=True, help_text='Requerido.')
    last_name = forms.CharField(max_length=150, required=True, help_text='Requerido.')
    telefono = forms.CharField(max_length=20, required=False, help_text='Opcional.')
    rol = forms.ModelChoiceField(queryset=Rol.objects.all(), required=True, help_text='Selecciona tu rol.')
    barrio = forms.ModelChoiceField(queryset=Sector.objects.all(), required=False, help_text='Opcional. Selecciona tu barrio.')

    class Meta:
        model = Usuario
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'telefono',
            'rol',
            'barrio',
            'password1',
            'password2',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email ya está registrado.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.barrio = self.cleaned_data.get('barrio')
        if commit:
            user.save()
        return user

class UsuarioRegistroPublicoForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido. Ingresa un email válido.')
    first_name = forms.CharField(max_length=30, required=True, help_text='Requerido.')
    last_name = forms.CharField(max_length=150, required=True, help_text='Requerido.')
    telefono = forms.CharField(max_length=20, required=False, help_text='Opcional.')
    barrio = forms.ModelChoiceField(queryset=Sector.objects.all(), required=False, help_text='Opcional. Selecciona tu barrio.')

    class Meta:
        model = Usuario
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'telefono',
            'barrio',
            'password1',
            'password2',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email ya está registrado.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.barrio = self.cleaned_data.get('barrio')
        
        # Asignar rol predeterminado de "Vecino"
        try:
            vecino_rol = Rol.objects.get(nombre='Vecino')
            user.rol = vecino_rol
        except Rol.DoesNotExist:
            pass
            
        if commit:
            user.save()
        return user


class UsuarioActualizarForm(UserChangeForm):
    password = None
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    telefono = forms.CharField(max_length=20, required=False)
    rol = forms.ModelChoiceField(queryset=Rol.objects.all(), required=False)
    barrio = forms.ModelChoiceField(queryset=Sector.objects.all(), required=False)

    class Meta:
        model = Usuario
        fields = [
            'first_name',
            'last_name',
            'email',
            'telefono',
            'barrio',
        ]


class UsuarioLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
