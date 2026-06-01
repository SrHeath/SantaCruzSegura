from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Alerta

from django.shortcuts import render, redirect
from django.contrib import messages
from incidentes.models import Sector
from .models import Alerta, SuscripcionAlerta

class AlertaListView(LoginRequiredMixin, ListView):
    model = Alerta
    template_name = 'alertas/lista.html'
    context_object_name = 'alertas'
    paginate_by = 20

    def get_queryset(self):
        return Alerta.objects.order_by('-fecha')

class SuscripcionAlertaConfigView(LoginRequiredMixin, ListView):
    model = Sector
    template_name = 'alertas/configurar.html'
    context_object_name = 'sectores'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener los IDs de sectores suscritos por el usuario actual
        suscritos = SuscripcionAlerta.objects.filter(usuario=self.request.user).values_list('sector_id', flat=True)
        context['suscritos_ids'] = list(suscritos)
        
        # Obtener la primera suscripcion para ver canal preferido y si recibe predictivas
        first_sub = SuscripcionAlerta.objects.filter(usuario=self.request.user).first()
        context['canal_preferido'] = first_sub.canal_preferido if first_sub else 'ambos'
        context['recibir_predictivas'] = first_sub.recibir_predictivas if first_sub else True
        return context

    def post(self, request):
        sectores_ids = request.POST.getlist('sectores')
        canal = request.POST.get('canal_preferido', 'ambos')
        predictivas = request.POST.get('recibir_predictivas') == 'on'
        
        # Eliminar las suscripciones anteriores que ya no estén seleccionadas
        SuscripcionAlerta.objects.filter(usuario=request.user).exclude(sector_id__in=sectores_ids).delete()
        
        # Crear o actualizar suscripciones
        for sid in sectores_ids:
            try:
                sector = Sector.objects.get(pk=sid)
                SuscripcionAlerta.objects.update_or_create(
                    usuario=request.user,
                    sector=sector,
                    defaults={
                        'canal_preferido': canal,
                        'recibir_predictivas': predictivas
                    }
                )
            except Sector.DoesNotExist:
                continue
                
        messages.success(request, "Configuración de suscripción a alertas guardada exitosamente.")
        return redirect('alerta_suscripcion_config')

