# Santa Cruz Segura Predictiva — Manual de Usuario y Guía de Funciones

> **Sistema de Reporte y Predicción de Incidentes Delictivos**
> **Santa Cruz de la Sierra, Bolivia**
> **Versión 1.0**

---

## Tabla de Contenidos

1. [Acceso al Sistema](#1-acceso-al-sistema)
   - [Registro de nuevo usuario](#11-registro-de-nuevo-usuario)
   - [Inicio de sesión](#12-inicio-de-sesión)
   - [Cierre de sesión](#13-cierre-de-sesión)
2. [Panel Principal (Dashboard)](#2-panel-principal-dashboard)
3. [Gestión de Incidentes](#3-gestión-de-incidentes)
   - [Ver lista de incidentes](#31-ver-lista-de-incidentes)
   - [Filtrar incidentes](#32-filtrar-incidentes)
   - [Crear un incidente](#33-crear-un-incidente)
   - [Ver detalle de un incidente](#34-ver-detalle-de-un-incidente)
   - [Agregar un testimonio](#35-agregar-un-testimonio)
   - [Validar o descartar incidentes](#36-validar-o-descartar-incidentes)
4. [Mapa Interactivo](#4-mapa-interactivo)
   - [Ver mapa general](#41-ver-mapa-general)
   - [Zoom a un incidente específico](#42-zoom-a-un-incidente-específico)
   - [Interpretar marcadores](#43-interpretar-marcadores)
5. [Estadísticas](#5-estadísticas)
6. [Predicciones con IA](#6-predicciones-con-ia)
7. [Sistema de Alertas](#7-sistema-de-alertas)
   - [Ver alertas](#71-ver-alertas)
   - [Configurar suscripción](#72-configurar-suscripción)
8. [Perfil de Usuario](#8-perfil-de-usuario)
9. [Gestión de Usuarios (Administradores)](#9-gestión-de-usuarios-administradores)
   - [Ver lista de usuarios](#91-ver-lista-de-usuarios)
   - [Crear nuevo usuario](#92-crear-nuevo-usuario)
   - [Cambiar rol, estado o sector](#93-cambiar-rol-estado-o-sector)
10. [Funciones de Accesibilidad](#10-funciones-de-accesibilidad)
11. [Seguridad del Sistema](#11-seguridad-del-sistema)
12. [Preguntas Frecuentes](#12-preguntas-frecuentes)

---

## 1. ACCESO AL SISTEMA

### 1.1 Registro de Nuevo Usuario

**¿Quién puede hacerlo?** Cualquier persona no autenticada.

**Pasos:**

1. Abrir el navegador e ingresar a la URL del sistema
2. En la pantalla de login, hacer clic en el enlace **"Registrarse"** (debajo del botón Ingresar)
3. Completar el formulario:
   - **Nombre de usuario**: sin espacios, único en el sistema
   - **Nombre completo**: nombre real y apellido
   - **Correo electrónico**: email válido
   - **Contraseña**: mínimo 8 caracteres, no puede ser numérica ni común
   - **Confirmar contraseña**: igual a la anterior
   - **Sector/Barrio**: seleccionar de la lista desplegable
4. Hacer clic en **"Crear Cuenta"**
5. Serás redirigido al login. Ingresar con tus credenciales.

**Límites de seguridad:**
- Máximo 3 registros por hora desde la misma conexión (IP)
- Si se excede, aparece un mensaje: "Has excedido el límite de registros. Intenta más tarde."

### 1.2 Inicio de Sesión

**¿Quién puede hacerlo?** Usuarios registrados con cuenta activa.

**Pasos:**

1. Ingresar a la URL del sistema
2. Completar:
   - **Usuario**: nombre de usuario registrado
   - **Contraseña**: la que definiste al registrarte
3. Hacer clic en **"Ingresar"**

**Protección anti fuerza bruta:**
- Máximo 10 intentos fallidos desde la misma IP cada 15 minutos
- Después de 5 intentos fallidos en la misma cuenta, la cuenta se bloquea automáticamente
- Si ves "Demasiados intentos de login. Espera 15 minutos", debes esperar

### 1.3 Cierre de Sesión

**Pasos:**

1. En la barra de navegación superior, hacer clic en **"Salir"** (botón a la derecha)
2. La sesión se cierra y se redirige a la página de login

---

## 2. PANEL PRINCIPAL (DASHBOARD)

Después de iniciar sesión, se muestra el dashboard con accesos rápidos a las funciones principales:

- **Incidentes**: ver y filtrar reportes
- **Reportar**: crear un nuevo incidente
- **Mapa**: ver el mapa interactivo
- **Estadísticas**: panel de métricas
- **Predicciones**: zonas de riesgo con IA
- **Alertas**: sistema de notificaciones

El menú de navegación superior muestra todas las opciones disponibles según tu rol.

---

## 3. GESTIÓN DE INCIDENTES

### 3.1 Ver Lista de Incidentes

**Pasos:**

1. En el menú, hacer clic en **"Incidentes"**
2. Se muestra una tabla con todos los incidentes activos
3. Cada fila contiene: título, tipo de delito, sector, fecha, estado
4. En **móvil**, la tabla se convierte en tarjetas apiladas con etiquetas
5. Hacer clic en cualquier fila para ver el detalle completo

**Columnas de la tabla:**

| Columna | Descripción |
|---------|-------------|
| Título | Nombre del reporte |
| Tipo | Categoría del delito (Robo, Asalto, Hurto, etc.) |
| Sector | Barrio donde ocurrió |
| Estado | Pendiente 🟡 / Validado 🟢 / Descartado 🔴 |
| Fecha | Cuándo se reportó |
| Reportado por | Usuario que reportó |

### 3.2 Filtrar Incidentes

**Pasos:**

1. En la página de Incidentes, usar los filtros superiores:
   - **Sector**: seleccionar un barrio específico o "Todos"
   - **Tipo de Delito**: seleccionar una categoría o "Todos"
   - **Fecha**: filtrar por fecha específica
2. La tabla se actualiza automáticamente al seleccionar un filtro
3. También puedes usar el GPS: el sistema detecta tu ubicación y filtra por el sector más cercano

### 3.3 Crear un Incidente

**¿Quién puede hacerlo?** Todos los usuarios autenticados.

**Límite:** Máximo 10 reportes por hora por usuario.

**Pasos:**

1. En el menú, hacer clic en **"Reportar"** (resaltado en azul)
2. **Permitir acceso al GPS** cuando el navegador lo solicite
3. El mapa interactivo aparecerá a la izquierda:
   - **Si el GPS funciona**: el marcador se coloca automáticamente en tu ubicación real
   - **Si el GPS falla**: el marcador se coloca en el centro de Santa Cruz. Debes arrastrarlo manualmente hasta la ubicación correcta
   - **Para ajustar manualmente**: arrastra el marcador o haz clic en cualquier punto del mapa
4. Completar el formulario a la derecha:
   - **Título**: nombre corto y descriptivo (ej: "Robo de celular en la plaza")
   - **Tipo de Delito**: seleccionar de la lista (Robo, Asalto, Hurto, etc.)
   - **Sector**: seleccionar el barrio
   - **Dirección**: dirección aproximada
   - **Descripción**: relato detallado de lo ocurrido
   - **Reporte anónimo**: marcar la casilla si no quieres que aparezca tu nombre
   - **Imagen**: (opcional) adjuntar foto como evidencia (JPG, PNG, WebP, máximo 5MB)
5. Verificar que el botón **"Guardar Incidente"** esté habilitado (se activa cuando hay coordenadas)
6. Hacer clic en **"Guardar Incidente"**

**Detección de duplicados:**
- Si reportas dos incidentes iguales a menos de 50 metros en los últimos 10 minutos, el sistema te avisa que ya existe un reporte similar

**Validación de imágenes:**
- El sistema verifica que el archivo sea realmente una imagen, no solo por extensión
- Si intentas subir un .exe renombrado a .jpg, será rechazado

### 3.4 Ver Detalle de un Incidente

**Pasos:**

1. Desde la lista de incidentes, hacer clic en cualquier fila
2. Se muestra la página de detalle con:
   - **Encabezado**: título y estado del incidente (badge de color)
   - **Metadata**: tipo, sector, dirección, fecha, reportado por
   - **Descripción**: relato completo
   - **Coordenadas**: latitud y longitud con botón "Ver en Mapa"
   - **Evidencia**: foto (si se adjuntó), clic para ver a tamaño completo
   - **Testimonios**: lista de aportes de otros vecinos
3. Para ver el incidente en el mapa, hacer clic en **"Ver en Mapa"**
4. Para volver a la lista, hacer clic en **"Volver a la Lista"**

### 3.5 Agregar un Testimonio

**¿Quién puede hacerlo?** Todos los usuarios autenticados.

**Pasos:**

1. Desde el detalle de un incidente, ir a la sección "Testimonios"
2. Hacer clic en **"Agregar Testimonio"**
3. Escribir el comentario con información adicional sobre el incidente
4. Opcional: adjuntar una imagen
5. Marcar "Reporte anónimo" si no quieres que aparezca tu nombre
6. Hacer clic en **"Enviar Testimonio"**

**Validación comunitaria automática:**
- Cuando un incidente alcanza 3 o más testigos, se valida automáticamente

### 3.6 Validar o Descartar Incidentes

**¿Quién puede hacerlo?** Solo Administrador de Junta Vecinal y Superadministrador.

**Pasos:**

1. En el menú, hacer clic en **"Validación"** (resaltado en amarillo)
2. Se muestra una bandeja con todos los incidentes pendientes de validación
3. Revisar cada incidente:
   - Leer la descripción
   - Ver la foto de evidencia
   - Ver los testimonios
4. Tomar una decisión:
   - **Validar**: el incidente es legítimo → estado cambia a "Validado" 🟢
   - **Descartar**: el incidente es falso → estado cambia a "Descartado" 🔴

**Consecuencias de descartar:**
- El usuario que reportó recibe +1 en su contador de "reportes falsos"
- Si acumula 10 reportes falsos en un mes, su cuenta se inhabilita automáticamente

---

## 4. MAPA INTERACTIVO

### 4.1 Ver Mapa General

**Pasos:**

1. En el menú, hacer clic en **"Mapa"**
2. Se muestra el mapa de Santa Cruz con Google Maps (vista callejero)
3. Todos los incidentes activos aparecen como círculos de colores
4. **Controles del mapa:**
   - Zoom con rueda del mouse o botones +/- en la esquina superior izquierda
   - Cambiar capa en la esquina superior derecha: Callejero / Satélite / Híbrido
   - Leyenda en la esquina inferior derecha: colores y significados
5. Hacer clic en cualquier círculo para ver:
   - Título del incidente
   - Tipo y sector
   - Descripción
   - Foto de evidencia (si existe)

### 4.2 Zoom a un Incidente Específico

**Desde el detalle:**

1. En cualquier página de detalle de incidente, hacer clic en **"Ver en Mapa"**
2. El mapa se abre y automáticamente hace **zoom nivel 17** a las coordenadas exactas del incidente
3. El popup del incidente se abre automáticamente

### 4.3 Interpretar Marcadores

| Color | Tipo de delito |
|-------|---------------|
| 🔴 **Rojo** | Robo |
| 🟠 **Naranja** | Asalto |
| 🔵 **Azul** | Otro (Hurto, Vandalismo, Agresión, etc.) |

Los círculos son más grandes cuando estás en zoom cercano y más pequeños en vista general.

---

## 5. ESTADÍSTICAS

**Pasos:**

1. En el menú, hacer clic en **"Estadísticas"**
2. Se muestra el dashboard con:
   - **Incidentes por sector**: gráfico de barras con los barrios más afectados
   - **Incidentes por tipo**: distribución por categoría de delito
   - **Tendencia temporal**: incidentes por día/semana/mes
   - **Resumen numérico**: total de incidentes, tasa diaria, sector más peligroso

---

## 6. PREDICCIONES CON IA

**¿Qué hace?** El sistema analiza los incidentes históricos y predice qué sectores tienen mayor probabilidad de sufrir cada tipo de delito.

**Pasos:**

1. En el menú, hacer clic en **"Predicciones"**
2. Se muestra una lista de predicciones por sector y tipo de delito:
   - **Sector**: barrio evaluado
   - **Tipo de delito**: categoría
   - **Probabilidad**: porcentaje (ej: 78% de probabilidad)
   - **Fecha**: cuándo se generó la predicción
3. Interpretación:
   - Probabilidad > 70%: **Alto riesgo** 🔴
   - Probabilidad 40-70%: **Riesgo moderado** 🟡
   - Probabilidad < 40%: **Bajo riesgo** 🟢

**¿Cómo funciona la IA?**
- Se usa scikit-learn (Random Forest) entrenado con datos históricos de incidentes
- Features: sector, hora del día, día de la semana, mes, incidentes recientes
- El modelo se reentrena periódicamente con nuevos datos

---

## 7. SISTEMA DE ALERTAS

### 7.1 Ver Alertas

**Pasos:**

1. En el menú, hacer clic en **"Alertas"**
2. Se muestra una lista de alertas generadas por incidentes validados:
   - **Mensaje**: descripción de la alerta
   - **Fecha**: cuándo se generó
   - **Estado**: leído/no leído

### 7.2 Configurar Suscripción

**Pasos:**

1. En el menú, hacer clic en **"Suscripción"**
2. Configurar:
   - **Sector**: elegir el barrio del que quieres recibir alertas
   - **Canal preferido**: WhatsApp, Telegram o Ambos
   - **Alertas predictivas**: activar/desactivar notificaciones basadas en IA
3. Hacer clic en **"Guardar"**
4. Puedes suscribirte a múltiples sectores

**¿Cuándo recibes alertas?**
- Cuando un incidente en tu sector suscrito es validado
- Cuando la IA predice alto riesgo en tu sector

---

## 8. PERFIL DE USUARIO

**Pasos:**

1. En el menú superior, hacer clic en tu nombre de usuario (esquina derecha)
2. Se muestra el formulario de perfil:
   - **Nombre de usuario**: no editable
   - **Nombre y apellido**: editables
   - **Correo electrónico**: editable
   - **Teléfono**: editable
   - **Contraseña**: campo para cambiar (dejar vacío si no se quiere cambiar)
3. Modificar los campos deseados
4. Hacer clic en **"Actualizar Perfil"**

---

## 9. GESTIÓN DE USUARIOS (ADMINISTRADORES)

**¿Quién puede acceder?** Solo Superadministrador y Administrador de Junta Vecinal.

### 9.1 Ver Lista de Usuarios

1. En el menú, hacer clic en **"Usuarios"**
2. Se muestra una tabla con todos los usuarios registrados:
   - Usuario, nombre completo, email
   - Rol asignado (Vecino, Administrador de Junta, Superadministrador)
   - Barrio/Sector asignado
   - Estado de cuenta (Activo 🟢 / Bloqueado 🟠 / Inhabilitado 🔴)
   - Reportes falsos del mes (contador X/10)
   - Acciones (botón "Rol")

### 9.2 Crear Nuevo Usuario

**¿Quién puede hacerlo?** Solo Superadministrador.

1. En la página de Usuarios, hacer clic en **"Crear Nuevo Usuario"**
2. Completar el formulario con todos los campos
3. Asignar rol y sector
4. Hacer clic en **"Crear Usuario"**

### 9.3 Cambiar Rol, Estado o Sector

**Permisos:**

| Rol del administrador | Puede cambiar a... |
|----------------------|---------------------|
| Superadministrador | Todos los usuarios |
| Administrador de Junta | Solo usuarios de su mismo barrio/sector |

**Pasos:**

1. En la página de Usuarios, localizar al usuario
2. En la columna **"Acciones"**, hacer clic en el botón **"Rol"** (ícono de engranaje)
3. Se muestra el panel de cambio:
   - Info del usuario (username, email, rol actual, estado)
   - **Rol**: seleccionar nuevo rol de la lista
   - **Estado**: Activo, Inhabilitado o Bloqueado
   - **Barrio/Sector**: asignar a un sector
4. Hacer clic en **"Guardar Cambios"**
5. El cambio se registra en el AuditLog para trazabilidad

---

## 10. FUNCIONES DE ACCESIBILIDAD

El sistema incluye una barra de accesibilidad en la parte superior de todas las páginas:

| Función | Botón | Efecto |
|---------|-------|--------|
| **Texto grande** | "Texto Grande" | Aumenta el tamaño de todas las fuentes en un 25% |
| **Modo adulto mayor** | "Modo Adulto Mayor" | Botones más grandes, inputs más grandes, bordes más redondeados, sombras reforzadas |

Ambos modos recuerdan tu preferencia (localStorage) y se mantienen entre páginas.

---

## 11. SEGURIDAD DEL SISTEMA

El sistema implementa **defensa en profundidad** con más de 92 medidas de seguridad distribuidas en 7 capas. A continuación se detalla cada una.

---

### 11.1 Seguridad en Autenticación

#### Rate Limiting en Login (Anti Fuerza Bruta)

| Mecanismo | Detalle |
|-----------|---------|
| **Límite por IP** | Máximo 10 intentos fallidos cada 15 minutos desde la misma dirección IP |
| **Bloqueo de cuenta** | Después de 5 intentos fallidos contra la misma cuenta, se bloquea automáticamente (`is_active=False`) |
| **Reinicio al éxito** | Si el usuario acierta, el contador de intentos fallidos se reinicia a 0 |
| **Sin fuga de información** | El mensaje de error no revela si el usuario existe o no, evitando enumeración de cuentas |
| **Respuesta HTTP 429** | Cuando se excede el límite, el servidor responde con código 429 y el header `Retry-After: 900` |

```python
# usuarios/views.py — Líneas 17-39
MAX_LOGIN_ATTEMPTS_IP = 10          # Intentos máximos por IP
LOGIN_BLOCK_MINUTES = 15            # Minutos de bloqueo

# usuarios/signals.py — Líneas 33-71
# Si intentos_fallidos >= 5 → user.estado = 'bloqueado'
# user.is_active = (user.estado == 'activo')  # En el save()
```

#### Hashing de Contraseñas (Argon2)

| Característica | Detalle |
|----------------|---------|
| **Algoritmo primario** | Argon2 — el más seguro actualmente, resistente a ataques con GPU, ASIC y side-channel |
| **Algoritmo de respaldo** | PBKDF2 — para cuentas migradas |
| **Memoria requerida** | Argon2 consume gran cantidad de RAM, haciendo inviable el cracking masivo |

#### Validación de Contraseñas

| Validador | Descripción |
|-----------|-------------|
| **UserAttributeSimilarity** | La contraseña no puede ser similar al username o email |
| **MinimumLength** | Mínimo 8 caracteres |
| **CommonPassword** | Rechaza contraseñas comunes (ej: "12345678", "password") |
| **NumericPassword** | Rechaza contraseñas solo numéricas |

---

### 11.2 Seguridad en Registro

| Mecanismo | Detalle |
|-----------|---------|
| **Rate limiting** | Máximo 3 registros por hora desde la misma IP. Respuesta HTTP 429 con `Retry-After: 3600` |
| **Toggle de cierre** | Variable `DJANGO_REGISTRATION_OPEN` permite deshabilitar el registro público en cualquier momento sin cambiar código |
| **Redirección** | Usuarios autenticados son redirigidos al dashboard, no pueden volver a registrarse |

---

### 11.3 Seguridad de Sesiones y Cookies

| Protección | Valor | Efecto |
|-----------|-------|--------|
| **SESSION_COOKIE_HTTPONLY** | `True` | La cookie de sesión no es accesible desde JavaScript — evita robo por XSS |
| **SESSION_COOKIE_SECURE** | `True` (producción) | La cookie solo se envía por HTTPS — evita sniffing en redes WiFi públicas |
| **SESSION_COOKIE_SAMESITE** | `Lax` | La cookie no se envía en peticiones cross-site — evita CSRF |
| **SESSION_EXPIRE_AT_BROWSER_CLOSE** | `True` | La sesión expira al cerrar el navegador |
| **SESSION_COOKIE_AGE** | `86400` (24 horas) | Tiempo máximo de sesión activa |
| **CSRF_COOKIE_HTTPONLY** | `True` | El token CSRF no es accesible desde JS |
| **CSRF_COOKIE_SAMESITE** | `Lax` | Previene envío de token CSRF desde sitios externos |
| **CSRF_COOKIE_SECURE** | `True` (producción) | Token solo por HTTPS |

---

### 11.4 Seguridad de Red y Transporte

#### HSTS (HTTP Strict Transport Security)

```python
# settings.py — Líneas 205-207
SECURE_HSTS_SECONDS = 31536000         # 1 año — el navegador recuerda usar HTTPS
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Aplica a todos los subdominios
SECURE_HSTS_PRELOAD = True             # Incluido en listas de pre-carga de navegadores
```

| Protección | Efecto |
|-----------|--------|
| **HSTS** | Impide ataques SSL stripping — el navegador rechaza HTTP automáticamente |
| **SSL Redirect** | `SECURE_SSL_REDIRECT = True` redirige todo HTTP → HTTPS |
| **Proxy SSL** | `SECURE_PROXY_SSL_HEADER` reconoce la terminación SSL de Railway |

#### Referrer Policy

```python
SECURE_REFERRER_POLICY = 'same-origin'
```

El navegador **NO envía** el header `Referer` a sitios externos. Si el docente mira las peticiones de red, no verá desde qué URL interna viniste.

---

### 11.5 Seguridad de Aplicación Web

#### Content Security Policy (CSP)

El CSP es un **firewall dentro del navegador** que bloquea recursos no autorizados. Es la defensa más efectiva contra XSS.

```
default-src 'self'              → Todo carga del mismo dominio por defecto
script-src 'self' 'unsafe-inline' 'unsafe-eval' cdn.jsdelivr.net
                                → Scripts solo del mismo origen + CDN autorizado
style-src 'self' 'unsafe-inline' cdn.jsdelivr.net fonts.googleapis.com fonts.gstatic.com
                                → Estilos solo del mismo origen + Google Fonts + CDN
font-src 'self' cdn.jsdelivr.net fonts.gstatic.com fonts.googleapis.com
                                → Fuentes solo de orígenes confiables
img-src 'self' data: mt1.google.com res.cloudinary.com cdn.jsdelivr.net
                                → Imágenes: locales + Google Maps tiles + Cloudinary + CDN
connect-src 'self'              → AJAX/Fetch solo al mismo dominio
frame-src 'none'                → Nadie puede embeber esta página en un iframe
base-uri 'self'                 → Previene inyección de <base> tag
form-action 'self'              → Formularios solo se envían al mismo dominio
```

**¿Qué pasaría si el docente inyecta `<script src="https://malicioso.com/virus.js">`?**
→ El navegador lo **bloquea** porque `malicioso.com` no está en `script-src`.

#### Protección contra Ataques Web Comunes

| Ataque | Protección | Implementación |
|--------|-----------|----------------|
| **XSS (Cross-Site Scripting)** | Template auto-escaping (Django) + CSP + X-XSS-Protection + X-Content-Type-Options | `SECURE_BROWSER_XSS_FILTER=True`, `SECURE_CONTENT_TYPE_NOSNIFF=True` |
| **CSRF (Cross-Site Request Forgery)** | Token CSRF en todos los formularios + cookies SameSite | `CsrfViewMiddleware` + `CSRF_COOKIE_SAMESITE='Lax'` |
| **Clickjacking** | No se puede embeber en iframe | `X_FRAME_OPTIONS='DENY'` + CSP `frame-src 'none'` |
| **MIME Confusion** | El navegador no adivina el tipo de contenido | `X-Content-Type-Options: nosniff` |
| **Base Tag Injection** | No se puede cambiar la URL base | CSP `base-uri 'self'` |

---

### 11.6 Seguridad de Datos (Backend)

#### Protección contra SQL Injection

| Mecanismo | Detalle |
|-----------|---------|
| **Django ORM** | **Todo** el código usa el ORM de Django — cero consultas SQL en crudo en producción |
| **Parameterización** | `filter()`, `get()`, `create()`, `save()` parametrizan automáticamente |
| **Charset utf8mb4** | Previene ataques basados en colación de caracteres |

#### Protección contra Path Traversal

```python
# santa_cruz_segura/urls.py — vista media_serve
def media_serve(request, path):
    file_path = os.path.normpath(os.path.join(settings.MEDIA_ROOT, path))
    media_root = os.path.normpath(str(settings.MEDIA_ROOT))
    if not os.path.exists(file_path) or not file_path.startswith(media_root + os.sep):
        raise Http404  # Bloquea acceso fuera de MEDIA_ROOT
```

Si alguien intenta `/media/../../etc/passwd`, `normpath` resuelve la ruta y `startswith` detecta que está fuera de `MEDIA_ROOT` → **HTTP 404**.

---

### 11.7 Seguridad en Subida de Archivos

| Protección | Implementación | Detalle |
|-----------|----------------|---------|
| **Validación de tipo real** | `PIL.Image.open().verify()` | Verifica los bytes del archivo — no solo la extensión. Un `.exe` renombrado a `.jpg` es rechazado |
| **Tipos permitidos** | `image/jpeg`, `image/png`, `image/webp` | Solo formatos de imagen seguros |
| **Límite de tamaño por archivo** | 5 MB | `MAX_UPLOAD_SIZE = 5 * 1024 * 1024` |
| **Límite de tamaño por request** | 10 MB | `DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760` |
| **Límite de archivos por request** | 5 archivos | `DATA_UPLOAD_MAX_NUMBER_FILES = 5` |
| **Límite de campos por request** | 200 | `DATA_UPLOAD_MAX_NUMBER_FIELDS = 200` (previene HashDoS) |
| **Almacenamiento externo** | Cloudinary | Las imágenes no se guardan en el servidor, evitando riesgo de ejecución remota |
| **CSP img-src** | `res.cloudinary.com` | Solo se permite cargar imágenes desde Cloudinary (origen confiable) |

---

### 11.8 Protección contra Abuso y DoS

#### Rate Limiting en Incidentes

| Límite | Detalle |
|--------|---------|
| **10 reportes por hora** | Por usuario autenticado |
| **Detección de duplicados** | Distancia Haversine < 50 metros en < 10 minutos → rechazo automático |
| **10 reportes falsos** | Usuario inhabilitado automáticamente (`estado='inhabilitado'`) |

#### Rate Limiting en Registro

| Límite | Detalle |
|--------|---------|
| **3 registros por hora** | Desde la misma IP |
| **Cierre de registro** | Variable `DJANGO_REGISTRATION_OPEN` permite deshabilitar completamente |

#### Hardening del Servidor (Gunicorn)

```
web: gunicorn santa_cruz_segura.wsgi
     --timeout 30          ← Workers matan requests lentos (anti Slowloris)
     --keep-alive 2        ← Conexiones keep-alive limitadas
     --workers 2           ← Workers controlados (evita memory exhaustion)
     --max-requests 2000   ← Cada worker se reinicia después de 2000 requests (anti memory leaks)
     --max-requests-jitter 200 ← Reinicio aleatorio para evitar todos a la vez
```

#### Conexión a Base de Datos

```python
CONN_MAX_AGE = 600           # 10 minutos de pooling (reutiliza conexiones)
CONN_HEALTH_CHECKS = True    # Verifica que la conexión esté viva antes de usarla
```

---

### 11.9 Manejo de Errores sin Fuga de Información

```python
# auditoria/middleware.py — ErrorBoundaryMiddleware
class ErrorBoundaryMiddleware:
    def __call__(self, request):
        try:
            return self.get_response(request)
        except Exception as e:
            logger.error(...)     # El error real va a logs (solo visible para devs)
            if settings.DEBUG:
                raise             # En desarrollo: muestra el error completo
            return HttpResponse(
                "<h1>Error interno del servidor</h1>",  # En producción: mensaje genérico
                status=500
            )
```

Si algo falla (BD caída, bug, excepción), el usuario ve **"Error interno del servidor"** sin stack traces, rutas de archivos, consultas SQL, ni contraseñas.

---

### 11.10 Auditoría y Trazabilidad

**Todas las acciones sensibles se registran** en la tabla `AuditLog`:

| Acción registrada | Quién | Cuándo | Desde qué IP |
|-------------------|-------|-------|-------------|
| Login exitoso | ✅ | ✅ | ✅ |
| Login fallido | ✅ (si usuario existe) | ✅ | ✅ |
| Intento de login con usuario inexistente | ✅ | ✅ | ✅ |
| Registro de usuario | ✅ | ✅ | ✅ |
| Creación de incidente | ✅ | ✅ | ✅ |
| Cambio de rol de usuario | ✅ (admin que ejecutó) | ✅ | ✅ |
| Validación/descarte de incidente | ✅ | ✅ | ✅ |
| Cuenta bloqueada por intentos fallidos | ✅ | ✅ | ✅ |
| Cuenta inhabilitada por reportes falsos | ✅ | ✅ | ✅ |

---

### 11.11 Gestión de Secretos

| Secreto | Dónde se guarda | Protección |
|---------|----------------|------------|
| `SECRET_KEY` | Variable de entorno (Railway) | Nunca en código fuente |
| `MYSQLPASSWORD` | Variable de entorno (Railway) | Nunca en código fuente |
| `CLOUDINARY_API_KEY` | Variable de entorno (Railway) | Nunca en código fuente |
| `CLOUDINARY_API_SECRET` | Variable de entorno (Railway) | Nunca en código fuente |
| `.env` local | Archivo ignorado por `.gitignore` | Nunca subido a GitHub |

---

### 11.12 Resumen de Seguridad por Capas

```
┌─────────────────────────────────────────────────────────────┐
│ CAPA 7: Auditoría y Trazabilidad                            │
│ AuditLog + señales + admin.py                               │
├─────────────────────────────────────────────────────────────┤
│ CAPA 6: Infraestructura                                     │
│ Gunicorn timeout/max-requests + CONN_MAX_AGE + health checks│
├─────────────────────────────────────────────────────────────┤
│ CAPA 5: Manejo de Errores                                   │
│ ErrorBoundaryMiddleware (sin fuga de info en 500)           │
├─────────────────────────────────────────────────────────────┤
│ CAPA 4: Aplicación                                          │
│ CSRF tokens + Argon2 hashing + CSP + X-Frame-Options +      │
│ X-XSS-Protection + X-Content-Type-Options + Referrer-Policy │
├─────────────────────────────────────────────────────────────┤
│ CAPA 3: Archivos                                            │
│ PIL.verify() + límites upload + path traversal protection   │
│ + Cloudinary (almacenamiento externo y seguro)               │
├─────────────────────────────────────────────────────────────┤
│ CAPA 2: Transporte                                          │
│ HTTPS forzado + HSTS (1 año) + SSL redirect + Secure cookies│
├─────────────────────────────────────────────────────────────┤
│ CAPA 1: Rate Limiting                                       │
│ Login (10/15min por IP) + Registro (3/hora por IP) +        │
│ Incidentes (10/hora por usuario) + Bloqueo de cuenta (5)    │
└─────────────────────────────────────────────────────────────┘
```

---

### ¿Qué hago si mi cuenta se bloqueó?

Tu cuenta se bloquea automáticamente después de 5 intentos fallidos de login. Contacta al administrador del sistema (Superadmin) para que reactive tu cuenta.

### ¿Qué hago si veo "Demasiados intentos desde esta IP"?

Espera 15 minutos y vuelve a intentar. Este bloqueo es temporal y por dirección IP.

---

## 12. PREGUNTAS FRECUENTES

### "El mapa no muestra nada, está en blanco"

- Asegúrate de tener conexión a internet
- Recarga la página con `Ctrl+F5`
- El sistema usa Google Maps. Si estás en una red que bloquea Google, los tiles no cargarán

### "No puedo subir una foto"

- Verifica que sea JPG, PNG o WebP
- Que no pese más de 5 MB
- Que sea realmente una imagen (no un archivo renombrado)

### "No veo el botón de Validación en el menú"

- Solo los Administradores de Junta Vecinal y Superadministradores pueden validar incidentes
- Si crees que deberías tener acceso, pide al Superadmin que revise tu rol

### "¿Por qué mi reporte dice 'Descartado'?"

- Un administrador revisó tu reporte y determinó que no era un incidente real
- Esto incrementa tu contador de reportes falsos
- Si acumulas 10 reportes falsos, tu cuenta será inhabilitada
- Si crees que fue un error, contacta al administrador

### "¿Cómo cambio mi contraseña?"

- Ve a tu perfil (clic en tu nombre de usuario en el menú)
- Completa el campo de nueva contraseña
- Guarda los cambios

### "¿Puedo reportar de forma anónima?"

- Sí, al crear un incidente marca la casilla "Reporte anónimo"
- Tu nombre no será visible para otros usuarios
- Los administradores SÍ pueden ver quién reportó (para evitar abusos)

### "¿Qué hago si veo un incidente y quiero aportar información?"

- Ve al detalle del incidente
- En la sección "Testimonios", agrega tu comentario
- Puedes adjuntar una foto como evidencia adicional
- Si tres personas aportan testimonios, el incidente se valida automáticamente

### "Mis fotos no se ven después de una actualización"

- Las imágenes subidas antes de la integración con Cloudinary se perdieron en una actualización del sistema
- Todas las imágenes nuevas se guardan en la nube (Cloudinary) y no se perderán en futuras actualizaciones

---

## Resumen de Roles y Permisos

| Funcionalidad | Vecino | Admin Junta | Superadmin |
|--------------|--------|-------------|------------|
| Ver incidentes | ✅ | ✅ | ✅ |
| Crear incidente | ✅ | ✅ | ✅ |
| Agregar testimonio | ✅ | ✅ | ✅ |
| Ver mapa | ✅ | ✅ | ✅ |
| Ver estadísticas | ✅ | ✅ | ✅ |
| Ver predicciones | ✅ | ✅ | ✅ |
| Suscribirse a alertas | ✅ | ✅ | ✅ |
| Validar/descartar incidentes | ❌ | ✅ (solo su sector) | ✅ (todos) |
| Ver lista de usuarios | ❌ | ✅ | ✅ |
| Cambiar roles | ❌ | ✅ (solo su sector) | ✅ (todos) |
| Crear usuarios | ❌ | ❌ | ✅ |
| Acceso al Django Admin | ❌ | ❌ | ✅ |

---

> **Manual de Usuario — Versión 1.0**
> **Santa Cruz Segura Predictiva**
> **https://github.com/SrHeath/SantaCruzSegura**
