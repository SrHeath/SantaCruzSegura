# Guía de Instalación y Configuración para Desarrolladores

Esta guía describe los pasos necesarios para desplegar y ejecutar el proyecto **Santa Cruz Segura Predictiva** en tu entorno local.

---

## 🛠️ Requisitos Previos
* **Python** (versión 3.11 o 3.12 recomendada).
* **MySQL Server** (versión 8.x).
* **Git** (opcional, para versionado).

---

## 🚀 Pasos para Desplegar el Proyecto

### 1. Configurar la Base de Datos en MySQL
Abre tu cliente de MySQL (consola, MySQL Workbench, phpMyAdmin, etc.) y ejecuta la creación de la base de datos y el usuario:

```sql
-- 1. Crear Base de Datos
CREATE DATABASE santa_cruz_segura CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 2. Crear Usuario
CREATE USER 'santacruz'@'localhost' IDENTIFIED BY 'TuPasswordSeguro';

-- 3. Conceder Permisos
GRANT ALL PRIVILEGES ON santa_cruz_segura.* TO 'santacruz'@'localhost';
FLUSH PRIVILEGES;
```

> [!NOTE]
> Si prefieres usar otro usuario (como `root`), recuerda actualizar los campos correspondientes en la configuración `DATABASES` dentro del archivo `santa_cruz_segura/settings.py`.

---

### 2. Configurar el Entorno Virtual (Venv)
Abre una terminal (PowerShell o CMD en Windows) dentro del directorio raíz del proyecto:

```powershell
# Crear entorno virtual de Python
python -m venv .venv

# Activar Entorno Virtual:
# -  si estas usando terminal PowerShell:
.\.venv\Scripts\Activate.ps1

# - si estas usando terminal usando (CMD):
.\.venv\Scripts\activate.bat



---

### 3. Instalar Dependencias
Una vez activado el entorno virtual, instala las dependencias de Python listadas en el archivo `requirements.txt`:

```powershell
pip install -r requirements.txt
```

---

### 4. Aplicar Migraciones
Ejecuta las migraciones de Django para crear las tablas correspondientes en tu servidor de MySQL local:

```powershell
python manage.py migrate
```

---

### 5. Sembrar Datos Iniciales
Carga los datos iniciales necesarios para el sistema (sectores geográficos con coordenadas, catálogo de delitos, roles predefinidos e incidentes validados de prueba):

```powershell
python manage.py crear_datos
```

Al terminar, se creará una cuenta de administrador por defecto:
* **Usuario:** `admin`
* **Contraseña:** `1234`

---

### 6. Entrenar el Modelo de Inteligencia Artificial (IA)
Para generar el archivo de serialización del modelo predictivo (`.pkl`) y habilitar el mapa de calor y análisis predictivo de zonas, ejecuta:

```powershell
python manage.py reentrenar_ia --force
```

---

### 7. Iniciar el Servidor Local
Por último, arranca el servidor de desarrollo de Django:

```powershell
python manage.py runserver
```

Ya puedes ingresar a la plataforma abriendo tu navegador en: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🛡️ Comandos de Mantenimiento y Verificación

* **Realizar Respaldo de Base de Datos:**
  ```powershell
  python manage.py respaldar_bd
  ```
  *(Este comando genera una exportación de la base de datos MySQL, la comprime en `.zip`, calcula su firma hash SHA-256 para seguridad y simula la transferencia al servidor secundario en `/backups_secundario/`)*.

* **Reentrenamiento Semanal Automático de la IA:**
  ```powershell
  python manage.py reentrenar_ia
  ```
