from django import forms
from django.core.exceptions import ValidationError
from PIL import Image

from .models import Incidente

MAX_UPLOAD_SIZE = 5 * 1024 * 1024
ALLOWED_CONTENT_TYPES = ['image/jpeg', 'image/png', 'image/webp']

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

    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')
        if imagen:
            if imagen.size > MAX_UPLOAD_SIZE:
                raise ValidationError('La imagen no debe superar los 5MB.')
            if hasattr(imagen, 'content_type') and imagen.content_type not in ALLOWED_CONTENT_TYPES:
                raise ValidationError('Solo se permiten imagenes JPEG, PNG o WebP.')
            try:
                img = Image.open(imagen)
                img.verify()
            except Exception:
                raise ValidationError('El archivo no es una imagen valida.')
            finally:
                imagen.seek(0)
        return imagen

