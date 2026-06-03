from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView, View

from .forms import IncidenteForm
from .models import Incidente, Sector, TipoDelito

class IncidenteListView(LoginRequiredMixin, ListView):
    model = Incidente
    template_name = 'incidentes/lista.html'
    context_object_name = 'incidentes'
    paginate_by = 20

    def get_queryset(self):
        queryset = Incidente.objects.filter(activo=True)
        
        sector_id = self.request.GET.get('sector')
        tipo_id = self.request.GET.get('tipo')
        fecha = self.request.GET.get('fecha')
        gps_lat = self.request.GET.get('gps_lat')
        gps_lng = self.request.GET.get('gps_lng')

        # Filtro GPS automático si no hay un sector seleccionado explícitamente
        if gps_lat and gps_lng and not sector_id:
            try:
                user_lat = float(gps_lat)
                user_lng = float(gps_lng)
                closest_sector = None
                min_dist = float('inf')
                
                for sec in Sector.objects.filter(centro_lat__isnull=False, centro_lon__isnull=False):
                    dist = math.sqrt((float(sec.centro_lat) - user_lat)**2 + (float(sec.centro_lon) - user_lng)**2)
                    if dist < min_dist:
                        min_dist = dist
                        closest_sector = sec
                
                if closest_sector:
                    queryset = queryset.filter(sector=closest_sector)
                    self.nearest_sector = closest_sector
            except ValueError:
                pass
        
        # Filtro de Sector explícito
        if sector_id and sector_id != 'all':
            queryset = queryset.filter(sector_id=sector_id)
            
        # Filtro de Tipo de Delito
        if tipo_id and tipo_id != 'all':
            queryset = queryset.filter(tipo_id=tipo_id)
            
        # Filtro de Fecha
        if fecha and fecha != 'all':
            from django.utils import timezone
            from datetime import timedelta
            now = timezone.now()
            if fecha == '24h':
                queryset = queryset.filter(fecha_hora__gte=now - timedelta(days=1))
            elif fecha == 'week':
                queryset = queryset.filter(fecha_hora__gte=now - timedelta(weeks=1))
            elif fecha == 'month':
                queryset = queryset.filter(fecha_hora__gte=now - timedelta(days=30))
                
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from incidentes.models import Sector, TipoDelito
        context['sectores'] = Sector.objects.all()
        context['tipos'] = TipoDelito.objects.all()
        context['selected_sector'] = self.request.GET.get('sector', 'all')
        context['selected_tipo'] = self.request.GET.get('tipo', 'all')
        context['selected_fecha'] = self.request.GET.get('fecha', 'all')
        
        if hasattr(self, 'nearest_sector'):
            context['nearest_sector'] = self.nearest_sector
            
        return context


import math
from datetime import timedelta
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import redirect
from .models import Testigo

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371.0  # Radio de la Tierra en km
    lat1_rad = math.radians(float(lat1))
    lon1_rad = math.radians(float(lon1))
    lat2_rad = math.radians(float(lat2))
    lon2_rad = math.radians(float(lon2))
    
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    return R * c * 1000  # Retorna en metros

class IncidenteCrearView(LoginRequiredMixin, CreateView):
    model = Incidente
    form_class = IncidenteForm
    template_name = 'incidentes/crear.html'
    success_url = reverse_lazy('incidente_lista')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            limite = timezone.now() - timedelta(hours=1)
            conteo = Incidente.objects.filter(
                reporte_por=self.request.user,
                fecha_hora__gte=limite
            ).count()
            if conteo >= 10:
                messages.error(self.request, "Has excedido el limite de 10 reportes por hora. Intenta mas tarde.")
                return redirect('incidente_lista')

        incidente_nuevo = form.save(commit=False)
        
        # Buscar duplicados creados en los últimos 10 minutos
        limite_tiempo = timezone.now() - timedelta(minutes=10)
        candidatos = Incidente.objects.filter(
            tipo=incidente_nuevo.tipo,
            activo=True,
            fecha_hora__gte=limite_tiempo
        )
        
        duplicado = None
        for cand in candidatos:
            dist = haversine_distance(
                incidente_nuevo.latitud, incidente_nuevo.longitud,
                cand.latitud, cand.longitud
            )
            if dist <= 50.0:  # 50 metros
                duplicado = cand
                break
        
        if duplicado:
            # Registrar como testigo con comentario e imagen adicionales (comportamiento de blog)
            Testigo.objects.create(
                incidente=duplicado,
                usuario=self.request.user,
                canal_origen='web',
                comentario=form.cleaned_data.get('descripcion'),
                imagen=self.request.FILES.get('imagen'),
                reporte_anonimo=form.cleaned_data.get('reporte_anonimo', False)
            )
            duplicado.num_testigos += 1
            
            # Auto-validación por consenso comunitario (3 o más testigos)
            if duplicado.num_testigos >= 3 and duplicado.estado == 'pendiente':
                duplicado.estado = 'validado'
                duplicado.fecha_hora_validacion = timezone.now()
                
                # Crear alerta automática
                from alertas.models import Alerta
                Alerta.objects.create(
                    incidente=duplicado,
                    mensaje=f"ALERTA CRÍTICA (Auto-validada por consenso): {duplicado.tipo.nombre} reportado en {duplicado.direccion}. Múltiples testigos lo confirman.",
                )
            
            duplicado.save()
            
            messages.info(
                self.request,
                f"Tu reporte coincide con uno existente. Hemos añadido tu descripción y foto como testimonio adicional en la sección de comentarios del incidente #{duplicado.pk}."
            )
            return redirect('incidente_detalle', pk=duplicado.pk)

        
        # Si no es duplicado, guardar como nuevo
        incidente_nuevo.reporte_por = self.request.user
        incidente_nuevo.save()
        messages.success(self.request, "Incidente registrado exitosamente.")
        return redirect(self.success_url)


class IncidenteDetalleView(LoginRequiredMixin, DetailView):
    model = Incidente
    template_name = 'incidentes/detalle.html'
    context_object_name = 'incidente'

class IncidenteMapaView(LoginRequiredMixin, TemplateView):
    template_name = 'incidentes/mapa.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['incidentes'] = Incidente.objects.filter(activo=True)
        return context


class IncidenteMapaAPIView(LoginRequiredMixin, View):
    def get(self, request):
        qs = Incidente.objects.filter(activo=True).select_related('tipo', 'sector')
        data = []
        for i in qs:
            data.append({
                'lat': float(i.latitud),
                'lng': float(i.longitud),
                'id': i.id,
                'titulo': i.titulo,
                'tipo': i.tipo.nombre,
                'sector': i.sector.nombre,
                'desc': i.descripcion[:200],
                'img': i.imagen.url if i.imagen else '',
            })
        return JsonResponse(data, safe=False)

from django.contrib.auth.mixins import UserPassesTestMixin
from alertas.models import Alerta, SuscripcionAlerta

class IncidenteBandejaValidacionView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Incidente
    template_name = 'incidentes/bandeja_validacion.html'
    context_object_name = 'incidentes'

    def test_func(self):
        if not self.request.user.is_authenticated:
            return False
        rol = getattr(self.request.user, 'rol', None)
        return rol and rol.nombre in ['Administrador de Junta', 'Superadministrador']

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or getattr(user.rol, 'nombre', None) == 'Superadministrador' or not getattr(user, 'barrio', None):
            return Incidente.objects.filter(estado='pendiente', activo=True)
        return Incidente.objects.filter(sector=user.barrio, estado='pendiente', activo=True)

class IncidenteValidarAccionView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        if not self.request.user.is_authenticated:
            return False
        rol = getattr(self.request.user, 'rol', None)
        return rol and rol.nombre in ['Administrador de Junta', 'Superadministrador']

    def post(self, request, pk, accion):
        from django.utils import timezone
        import sys
        
        try:
            incidente = Incidente.objects.get(pk=pk, activo=True)
        except Incidente.DoesNotExist:
            messages.error(request, "El incidente no existe o ha sido desactivado.")
            return redirect('incidente_lista')

        if accion == 'validar':
            incidente.estado = 'validado'
            incidente.validador = request.user
            incidente.fecha_hora_validacion = timezone.now()
            incidente.save()
            
            # Crear alerta y simular el envío por canales de suscripción
            alerta = Alerta.objects.create(
                incidente=incidente,
                mensaje=f"ALERTA INMEDIATA: {incidente.tipo.nombre} reportado en {incidente.direccion}. Validado por Junta Vecinal. Evite la zona.",
                creado_por=request.user
            )
            
            # Simulación de push API
            suscripciones = SuscripcionAlerta.objects.filter(sector=incidente.sector)
            print(f"Enviando alertas a {suscripciones.count()} vecinos suscritos al sector {incidente.sector.nombre}...", file=sys.stderr)
            for sub in suscripciones:
                # Simular envío segun canal_preferido
                print(f"  [PUSH] Enviando alerta a {sub.usuario.username} vía {sub.canal_preferido}...", file=sys.stderr)
                
            messages.success(request, f"Incidente #{incidente.pk} validado exitosamente. Alertas emitidas a los vecinos.")
        
        elif accion == 'rechazar':
            incidente.estado = 'falso'
            incidente.validador = request.user
            incidente.fecha_hora_validacion = timezone.now()
            incidente.save()
            
            # Control de reportes falsos
            reporter = incidente.reporte_por
            if reporter:
                reporter.reportes_falsos_mes += 1
                detalles_usuario = f"El usuario {reporter.username} ha acumulado {reporter.reportes_falsos_mes}/10 reportes falsos."
                if reporter.reportes_falsos_mes >= 10:
                    reporter.estado = 'inhabilitado'
                    detalles_usuario += " Cuenta inhabilitada temporalmente."
                reporter.save()
                
                # Crear log de auditoría del reportero
                from auditoria.models import AuditLog
                from auditoria.middleware import get_client_ip
                AuditLog.objects.create(
                    usuario=reporter,
                    accion='Inhabilitación de usuario' if reporter.estado == 'inhabilitado' else 'Incremento de reportes falsos',
                    modelo='Usuario',
                    registro_id=reporter.pk,
                    detalles=detalles_usuario,
                    ip_origen=get_client_ip(request)
                )

            messages.warning(request, f"Incidente #{incidente.pk} marcado como FALSO.")
        
        return redirect('incidente_bandeja_validacion')

