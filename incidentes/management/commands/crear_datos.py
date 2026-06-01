from django.core.management.base import BaseCommand
from django.utils import timezone
from decimal import Decimal
from incidentes.models import Sector, TipoDelito, Incidente
from usuarios.models import Usuario, Rol


class Command(BaseCommand):
    help = 'Crea datos de prueba para el proyecto'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Iniciando creación de datos...'))
        
        # Crear sectores con coordenadas
        sectores_data = [
            {'nombre': 'Plan 3.000', 'lat': -17.8222, 'lon': -63.1361},
            {'nombre': 'Los Lotes', 'lat': -17.8389, 'lon': -63.1722},
            {'nombre': 'El Remanso', 'lat': -17.7278, 'lon': -63.1611},
            {'nombre': 'Villa 1° de Mayo', 'lat': -17.7889, 'lon': -63.1333},
            {'nombre': 'Palmar del Oratorio', 'lat': -17.8833, 'lon': -63.1500},
            {'nombre': 'Equipetrol', 'lat': -17.7639, 'lon': -63.1944},
            {'nombre': 'Centro', 'lat': -17.7833, 'lon': -63.1821},
            {'nombre': 'Norte', 'lat': -17.7400, 'lon': -63.1650},
            {'nombre': 'Sur', 'lat': -17.8250, 'lon': -63.1950},
            {'nombre': 'Oeste', 'lat': -17.7950, 'lon': -63.2200},
        ]
        
        for s in sectores_data:
            Sector.objects.get_or_create(
                nombre=s['nombre'],
                defaults={
                    'centro_lat': Decimal(str(s['lat'])),
                    'centro_lon': Decimal(str(s['lon']))
                }
            )
        self.stdout.write(self.style.SUCCESS(f'OK: {len(sectores_data)} sectores creados'))
        
        # Crear tipos de delito
        tipos_data = [
            'Robo',
            'Asalto',
            'Hurto',
            'Fraude',
            'Violencia',
            'Vandalismo',
            'Tráfico de drogas',
            'Extorsión',
        ]
        
        for nombre in tipos_data:
            TipoDelito.objects.get_or_create(nombre=nombre)
        self.stdout.write(self.style.SUCCESS(f'OK: {len(tipos_data)} tipos de delito creados'))
        
        # Crear roles si no existen
        roles_data = [
            'Superadministrador',
            'Administrador de Junta',
            'Policía',
            'Vecino',
        ]
        
        for nombre in roles_data:
            Rol.objects.get_or_create(nombre=nombre)
        self.stdout.write(self.style.SUCCESS(f'OK: {len(roles_data)} roles creados'))
        
        # Crear incidentes de prueba
        sectores = Sector.objects.all()
        tipos = TipoDelito.objects.all()
        
        # Crear usuario admin si no existe
        usuario, created = Usuario.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@localhost.com',
                'first_name': 'Admin',
                'last_name': 'Sistema',
                'is_staff': True,
                'is_superuser': True,
                'rol': Rol.objects.get(nombre='Superadministrador')
            }
        )
        if created:
            usuario.set_password('1234')
            usuario.save()
            self.stdout.write(self.style.SUCCESS('OK: Superusuario admin creado (Pass: 1234)'))
        
        if sectores.exists() and tipos.exists():
            coordenadas = [
                (-17.8225, -63.1365),  # Plan 3.000
                (-17.8385, -63.1725),  # Los Lotes
                (-17.7275, -63.1615),  # El Remanso
                (-17.7885, -63.1335),  # Villa 1° de Mayo
                (-17.8835, -63.1505),  # Palmar del Oratorio
                (-17.7635, -63.1945),  # Equipetrol
                (-17.7835, -63.1825),  # Centro
                (-17.7405, -63.1655),  # Norte
                (-17.8255, -63.1955),  # Sur
                (-17.7955, -63.2205),  # Oeste
            ]
            
            for i, coords in enumerate(coordenadas):
                # Usar el sector correspondiente
                sec = sectores[i % sectores.count()]
                if not Incidente.objects.filter(
                    latitud=coords[0],
                    longitud=coords[1]
                ).exists():
                    Incidente.objects.create(
                        titulo=f'Incidente de prueba {i+1}',
                        descripcion=f'Este es un incidente de prueba número {i+1} en el sector {sec.nombre}',
                        latitud=Decimal(str(coords[0])),
                        longitud=Decimal(str(coords[1])),
                        direccion=f'Avenida Principal, {sec.nombre}',
                        sector=sec,
                        tipo=tipos.order_by('?').first(),
                        reporte_por=usuario,
                        activo=True,
                        estado='validado', # Marcar como validado para que sirva al entrenamiento de la IA
                        num_testigos=3
                    )
            
            self.stdout.write(self.style.SUCCESS(f'OK: {len(coordenadas)} incidentes de prueba creados'))
        
        self.stdout.write(self.style.SUCCESS('OK: Datos creados exitosamente'))


