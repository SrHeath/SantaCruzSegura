import os
import zipfile
import hashlib
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import connection
from auditoria.models import AuditLog

class Command(BaseCommand):
    help = 'Realiza un respaldo de la base de datos MySQL, lo comprime y lo transfiere al servidor secundario'

    def handle(self, *args, **options):
        # Directorios de backup
        backup_dir = os.path.join(settings.BASE_DIR, 'backups_local')
        secondary_dir = os.path.join(settings.BASE_DIR, 'backups_secundario')

        for d in [backup_dir, secondary_dir]:
            if not os.path.exists(d):
                os.makedirs(d)

        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        sql_filename = f"backup_{stamp}.sql"
        sql_filepath = os.path.join(backup_dir, sql_filename)
        zip_filename = f"backup_{stamp}.zip"
        zip_filepath = os.path.join(backup_dir, zip_filename)
        sec_filepath = os.path.join(secondary_dir, zip_filename)

        db_config = settings.DATABASES['default']
        db_name = db_config['NAME']
        
        self.stdout.write("Iniciando volcado de base de datos...")
        
        # Intenta hacer volcado usando mysqldump, si no, fallback a exportador Python
        dump_success = False
        try:
            # mysqldump -u username -p'password' -h host dbname > backup.sql
            user = db_config['USER']
            password = db_config['PASSWORD']
            host = db_config['HOST']
            port = db_config['PORT']
            
            # Construir comando
            cmd = f'mysqldump -u {user} -p"{password}" -h {host} --port={port} {db_name} > "{sql_filepath}"'
            ret = os.system(cmd)
            if ret == 0 and os.path.exists(sql_filepath) and os.path.getsize(sql_filepath) > 0:
                dump_success = True
                self.stdout.write(self.style.SUCCESS("mysqldump completado con éxito."))
        except Exception as e:
            self.stdout.write(self.style.WARNING(f"mysqldump falló o no disponible: {e}. Usando fallback de exportación..."))

        if not dump_success:
            # Fallback a exportador nativo de Python para garantizar funcionamiento
            try:
                with open(sql_filepath, 'w', encoding='utf-8') as f:
                    f.write(f"-- Santa Cruz Segura Predictiva SQL Backup\n")
                    f.write(f"-- Generado: {datetime.now()}\n")
                    f.write(f"-- DB: {db_name}\n\n")
                    
                    with connection.cursor() as cursor:
                        # Obtener tablas
                        cursor.execute("SHOW TABLES")
                        tables = [row[0] for row in cursor.fetchall()]
                        
                        for table in tables:
                            # Ignorar tablas de sistema si se prefiere, o exportar todo
                            f.write(f"-- Tabla: {table}\n")
                            cursor.execute(f"SHOW CREATE TABLE `{table}`")
                            create_sql = cursor.fetchone()[1]
                            f.write(f"{create_sql};\n\n")
                            
                            cursor.execute(f"SELECT * FROM `{table}`")
                            rows = cursor.fetchall()
                            if rows:
                                f.write(f"INSERT INTO `{table}` VALUES \n")
                                values_list = []
                                for row in rows:
                                    row_vals = []
                                    for val in row:
                                        if val is None:
                                            row_vals.append("NULL")
                                        elif isinstance(val, (int, float)):
                                            row_vals.append(str(val))
                                        else:
                                            # Escapar strings
                                            escaped = str(val).replace("'", "''").replace("\\", "\\\\")
                                            row_vals.append(f"'{escaped}'")
                                    values_list.append("(" + ", ".join(row_vals) + ")")
                                f.write(",\n".join(values_list) + ";\n\n")
                dump_success = True
                self.stdout.write(self.style.SUCCESS("Fallback de exportación completado con éxito."))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error crítico en exportación de base de datos: {e}"))
                AuditLog.objects.create(
                    usuario=None,
                    accion='Respaldo de BD fallido',
                    modelo='Sistema',
                    detalles=f"Fallo al respaldar base de datos: {e}",
                    ip_origen='127.0.0.1'
                )
                return

        # 2. Comprimir en ZIP
        try:
            with zipfile.ZipFile(zip_filepath, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(sql_filepath, arcname=sql_filename)
            # Eliminar SQL sin comprimir
            os.remove(sql_filepath)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error comprimiendo backup: {e}"))
            return

        # 3. Calcular Checksum SHA-256
        sha256 = hashlib.sha256()
        try:
            with open(zip_filepath, 'rb') as f:
                while chunk := f.read(8192):
                    sha256.update(chunk)
            checksum = sha256.hexdigest()
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error calculando checksum: {e}"))
            return

        # 4. Copiar al servidor secundario (simulado)
        try:
            with open(zip_filepath, 'rb') as f_src:
                with open(sec_filepath, 'wb') as f_dest:
                    f_dest.write(f_src.read())
            self.stdout.write(self.style.SUCCESS(f"Backup transferido a servidor secundario."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error en transferencia a servidor secundario: {e}"))
            AuditLog.objects.create(
                usuario=None,
                accion='Respaldo BD - Error transferencia',
                modelo='Sistema',
                detalles=f"Backup local creado pero falló transferencia a secundario: {e}",
                ip_origen='127.0.0.1'
            )
            return

        # 5. Eliminar backups locales y secundarios con más de 7 días de antigüedad
        limite_antiguedad = datetime.now() - timedelta(days=7)
        for folder in [backup_dir, secondary_dir]:
            for f in os.listdir(folder):
                filepath = os.path.join(folder, f)
                if os.path.isfile(filepath):
                    mtime = datetime.fromtimestamp(os.path.getmtime(filepath))
                    if mtime < limite_antiguedad:
                        try:
                            os.remove(filepath)
                            self.stdout.write(f"Eliminado backup antiguo: {f}")
                        except Exception as e:
                            self.stdout.write(f"No se pudo eliminar {f}: {e}")

        # 6. Registrar en AuditLog
        size_kb = os.path.getsize(zip_filepath) / 1024
        AuditLog.objects.create(
            usuario=None,
            accion='Respaldo de BD exitoso',
            modelo='Sistema',
            detalles=f"Respaldo automático exitoso. Archivo: {zip_filename} ({size_kb:.2f} KB). Checksum SHA256: {checksum}",
            ip_origen='127.0.0.1'
        )
        self.stdout.write(self.style.SUCCESS(f"Proceso completado. Checksum: {checksum}"))
