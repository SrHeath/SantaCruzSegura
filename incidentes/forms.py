from django import forms

from .models import Incidente

class IncidenteForm(forms.ModelForm):
    class Meta:
        model = Incidente
        fields = [
            'titulo',
            'descripcion',
            'latitud',
            'longitud',
            'direccion',
            'sector',
            'tipo',
            'imagen',
            'reporte_anonimo',
        ]

        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
            'latitud': forms.HiddenInput(),
            'longitud': forms.HiddenInput(),
        }

