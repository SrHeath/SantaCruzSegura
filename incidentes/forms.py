from django import forms
from django.core.exceptions import ValidationError
from PIL import Image
from io import BytesIO

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
        if not imagen:
            return imagen
        if imagen.size > MAX_UPLOAD_SIZE:
            raise ValidationError('La imagen no debe superar los 5MB.')
        try:
            content = BytesIO(imagen.read())
            img = Image.open(content)
            img.verify()
        except Exception:
            raise ValidationError('El archivo no es una imagen valida.')
        finally:
            imagen.seek(0)
        return imagen

