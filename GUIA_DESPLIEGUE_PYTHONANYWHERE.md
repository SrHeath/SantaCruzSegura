# Guia de Despliegue en PythonAnywhere

## Requisitos
- Cuenta en PythonAnywhere (plan gratuito o superior)
- Repositorio GitHub con el proyecto (opcional pero recomendado)

---

## Paso 1: Preparar el entorno local

### 1.1 Verificar que el proyecto esta listo
Asegurate de haber hecho commit de todos los cambios:
```bash
git status
git log --oneline -1
```

### 1.2 Subir el proyecto a GitHub (si no lo has hecho)
```bash
git remote add origin https://github.com/TU_USUARIO/santa_cruz_segura.git
git push -u origin master
```

---

## Paso 2: Configurar PythonAnywhere

### 2.1 Crear el entorno virtual
Desde la consola Bash de PythonAnywhere:
```bash
mkvirtualenv --python=/usr/bin/python3.11 santa-cruz-virtualenv
```

### 2.2 Instalar dependencias
```bash
pip install django>=5.2
pip install mysqlclient>=2.1
pip install pymysql>=1.0
pip install scikit-learn>=1.4
pip install pandas>=2.0
pip install reportlab>=4.0
pip install django-crispy-forms>=2.0
pip install crispy-bootstrap5
pip install Pillow>=10.0
pip install python-dotenv>=1.0
```

O simplemente:
```bash
pip install -r requirements.txt
```

### 2.3 Clonar el repositorio
```bash
git clone https://github.com/TU_USUARIO/santa_cruz_segura.git
cd santa_cruz_segura
```

---

## Paso 3: Configurar la base de datos MySQL

### 3.1 Crear la base de datos
Desde la consola Bash de PythonAnywhere:
```bash
mysql -u TU_USUARIO -p
```
Ingresa tu password de MySQL de PythonAnywhere.

Ejecuta:
```sql
CREATE DATABASE TU_USUARIO$santa_cruz_segura CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;
```

### 3.2 Configurar variables de entorno
En el panel de PythonAnywhere, ve a la pestaña **Web** y busca la seccion **Environment variables**. Agrega:

| Variable | Valor |
|---|---|
| `DJANGO_SECRET_KEY` | Tu clave secreta (generada anteriormente) |
| `DJANGO_DEBUG` | `False` |
| `DJANGO_ALLOWED_HOSTS` | `TU_USUARIO.pythonanywhere.com` |
| `DB_NAME` | `TU_USUARIO$santa_cruz_segura` |
| `DB_USER` | `TU_USUARIO` |
| `DB_PASSWORD` | Tu password de MySQL de PythonAnywhere |
| `DB_HOST` | `TU_USUARIO.mysql.pythonanywhere.com` |
| `DB_PORT` | `3306` |

---

## Paso 4: Configurar la Web App

### 4.1 Crear la web app
Ve a la pestaña **Web** > **Add a new web app**:
1. Elige **Manual Configuration**
2. Selecciona **Python 3.11**
3. En la seccion **Virtualenv**, ingresa: `santa-cruz-virtualenv`

### 4.2 Editar el archivo WSGI
Haz clic en el enlace del archivo WSGI (algo como `/var/www/TU_USUARIO_pythonanywhere_com_wsgi.py`) y reemplazalo con:

```python
import os
import sys

path = '/home/TU_USUARIO/santa_cruz_segura'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'santa_cruz_segura.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

Guarda y cierra.

### 4.3 Configurar archivos estaticos
En la misma pagina de la web app, ve a la seccion **Static files** y agrega:

| URL | Directory |
|---|---|
| `/static/` | `/home/TU_USUARIO/santa_cruz_segura/staticfiles` |

---

## Paso 5: Ejecutar migraciones y configurar

Desde la consola Bash:
```bash
cd ~/santa_cruz_segura
source ~/.virtualenvs/santa-cruz-virtualenv/bin/activate
python manage.py migrate
python manage.py crear_datos
python manage.py reentrenar_ia --force
python manage.py collectstatic --noinput
```

---

## Paso 6: Recargar y verificar

1. Ve a la pestaña **Web**
2. Haz clic en el boton **Reload** para tu web app
3. Visita `https://TU_USUARIO.pythonanywhere.com`
4. Verifica que CSS/JS cargan correctamente
5. Login con: `admin` / `1234`

---

## Solucion de problemas

### Error: No module named 'django'
Asegurate de que el virtualenv esta correctamente configurado en la pestana Web.

### Error: Database connection failed
Verifica las variables de entorno de la base de datos.

### Archivos estaticos no cargan
Ejecuta `python manage.py collectstatic --noinput` y verifica la configuracion de archivos estaticos en el panel Web.

### Error 500 en produccion
Revisa el **error log** en la pestana Web.

---

## Notas importantes

- **Media files**: En el plan gratuito, no puedes modificar archivos media. Para subir imagenes, necesitaras el plan pago o usar un servicio externo (S3, Cloudinary).
- **Modelo ML**: El modelo se reentrena en el servidor. No subas archivos `.pkl` al repositorio.
- **Seguridad**: Asegurate de que `DJANGO_DEBUG=False` en produccion.