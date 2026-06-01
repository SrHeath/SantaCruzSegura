from django.core.management.base import BaseCommand
from predicciones.ml import retrain_model_automatic

class Command(BaseCommand):
    help = 'Entrena el modelo de IA predictivo con los incidentes validados'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Fuerza el entrenamiento incluso si hay menos de 100 incidentes validados',
        )

    def handle(self, *args, **options):
        force = options['force']
        self.stdout.write("Iniciando entrenamiento del modelo IA...")
        exito, msg = retrain_model_automatic(force=force)
        
        if exito:
            self.stdout.write(self.style.SUCCESS(msg))
        else:
            self.stdout.write(self.style.WARNING(msg))
