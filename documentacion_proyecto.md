# Documentación del Proyecto: Santa Cruz Segura Predictiva

> **Sistema de Reporte y Predicción de Incidentes Delictivos para la Ciudad de Santa Cruz de la Sierra, Bolivia**

---

## Tabla de Contenidos

1. [Introducción](#1-introducción)
2. [Especificación de Requisitos](#2-especificación-de-requisitos)
   - 2.1 [Requisitos Funcionales](#21-requisitos-funcionales)
   - 2.2 [Requisitos No Funcionales](#22-requisitos-no-funcionales)
   - 2.3 [Actores del Sistema](#23-actores-del-sistema)
   - 2.4 [Diagrama de Casos de Uso](#24-diagrama-de-casos-de-uso)
   - 2.5 [Diagrama de Objetos](#25-diagrama-de-objetos)
3. [Diseño de Base de Datos](#3-diseño-de-base-de-datos)
   - 3.1 [Modelo Conceptual (Diagrama Entidad-Relación)](#31-modelo-conceptual-diagrama-entidad-relación)
   - 3.2 [Modelo Lógico (Tablas)](#32-modelo-lógico-tablas)
   - 3.3 [Modelo Físico (Script SQL)](#33-modelo-físico-script-sql)
4. [Planificación del Desarrollo](#4-planificación-del-desarrollo)
   - 4.1 [Metodología Seleccionada (SCRUM)](#41-metodología-seleccionada-scrum)
   - 4.2 [Objetivos SMART](#42-objetivos-smart)
   - 4.3 [Herramientas de Desarrollo](#43-herramientas-de-desarrollo)
   - 4.4 [Matriz RACI](#44-matriz-raci)
   - 4.5 [Estimación de Tiempos](#45-estimación-de-tiempos)
   - 4.6 [Alcance (MVP y MoSCoW)](#46-alcance-mvp-y-moscow)
   - 4.7 [Plan de Contingencias](#47-plan-de-contingencias)
   - 4.8 [Cronograma de Sprints](#48-cronograma-de-sprints)
5. [Desarrollo Técnico](#5-desarrollo-técnico)
   - 5.1 [Configuración de Ambientes](#51-configuración-de-ambientes)
   - 5.2 [Conexión a Base de Datos](#52-conexión-a-base-de-datos)
   - 5.3 [Implementación de CRUD](#53-implementación-de-crud)
   - 5.4 [Diseño de Interfaces de Usuario](#54-diseño-de-interfaces-de-usuario)
   - 5.5 [Integración de IA Predictiva](#55-integración-de-ia-predictiva)
6. [Pruebas y Testeo](#6-pruebas-y-testeo)
7. [Conclusiones y Recomendaciones](#7-conclusiones-y-recomendaciones)
8. [Referencias Bibliográficas](#8-referencias-bibliográficas)
9. [Anexos](#9-anexos)

---

## 1. INTRODUCCIÓN

### 1.1 Contexto

La ciudad de Santa Cruz de la Sierra, la más poblada de Bolivia con aproximadamente 2 millones de habitantes, enfrenta desafíos considerables en materia de seguridad ciudadana. Los vecinos de los diferentes barrios y distritos necesitan una herramienta accesible, moderna y confiable para reportar incidentes delictivos, visualizar las zonas de mayor riesgo y recibir alertas predictivas basadas en datos históricos.

### 1.2 Problema

Actualmente no existe una plataforma centralizada que permita:

- A los ciudadanos reportar incidentes con ubicación georreferenciada mediante GPS y evidencia fotográfica
- A las juntas vecinales validar y gestionar reportes de sus respectivas zonas
- Visualizar en un mapa interactivo la concentración de delitos por tipo y sector
- Obtener predicciones mediante inteligencia artificial sobre zonas con mayor probabilidad de incidentes

### 1.3 Solución Propuesta

**Santa Cruz Segura Predictiva** es una aplicación web desarrollada con Django 5.2 que implementa:

- **Registro y autenticación de usuarios** con roles diferenciados (Vecino, Administrador de Junta Vecinal, Superadministrador)
- **Reporte de incidentes georreferenciados** con captura automática de coordenadas GPS y subida de evidencia fotográfica a Cloudinary
- **Mapa interactivo de incidentes** sobre Google Maps mediante la biblioteca Leaflet.js
- **Sistema de validación comunitaria** mediante testigos y administradores de junta
- **Predicción de zonas de riesgo** utilizando machine learning (scikit-learn)
- **Alertas y suscripciones** por sector geográfico
- **Múltiples capas de seguridad informática** para proteger los datos de los ciudadanos

### 1.4 Objetivo General

Desarrollar una plataforma web segura y accesible que permita a los ciudadanos de Santa Cruz de la Sierra reportar incidentes delictivos de forma georreferenciada, visualizar las zonas de mayor riesgo en un mapa interactivo y recibir predicciones basadas en inteligencia artificial, contribuyendo a la seguridad ciudadana mediante la participación comunitaria.

### 1.5 Objetivos Específicos

1. Implementar un sistema de autenticación con roles y permisos diferenciados
2. Desarrollar un módulo de reporte de incidentes con geolocalización GPS y evidencia fotográfica
3. Construir un mapa interactivo con marcadores por tipo de delito
4. Integrar un motor de predicción basado en IA para anticipar zonas de riesgo
5. Establecer un flujo de validación comunitaria de incidentes
6. Configurar múltiples capas de seguridad informática (CSP, HSTS, rate limiting, Argon2, auditoría)

### 1.6 Tecnologías Utilizadas

| Categoría | Tecnología | Versión | Propósito |
|-----------|-----------|---------|-----------|
| **Backend** | Django | 5.2 | Framework web principal |
| **Base de Datos** | MySQL | 8.0 | Almacenamiento relacional |
| **Servidor** | Gunicorn | 23.0 | Servidor WSGI |
| **Despliegue** | Railway | — | Plataforma cloud (PaaS) |
| **Estáticos** | WhiteNoise | 6.6 | Servicio de archivos estáticos |
| **Imágenes** | Cloudinary | — | Almacenamiento externo de imágenes |
| **Mapas** | Leaflet.js | 1.9.4 | Visualización cartográfica |
| **Tiles** | Google Maps | — | Capa de mapa satelital/callejero |
| **ML** | scikit-learn | 1.4 | Modelos predictivos |
| **Frontend** | Bootstrap 5 | 5.3 | Framework CSS responsivo |
| **Íconos** | Bootstrap Icons | 1.11.3 | Íconos vectoriales |
| **Tipografía** | Outfit + Inter | — | Fuentes web de Google Fonts |
| **Hasher** | Argon2 | 23.1 | Hashing de contraseñas |
| **CSP** | Django CSP Middleware | — | Políticas de seguridad de contenido |

---

## 1.7 Arquitectura del Proyecto

```
santa_cruz_segura/
│
├── manage.py                        # Gestor de Django
├── requirements.txt                 # Dependencias del proyecto
├── Procfile                         # Configuración de Gunicorn para Railway
├── runtime.txt                      # Versión de Python para Railway
├── .env.example                     # Plantilla de variables de entorno
│
├── santa_cruz_segura/              # Configuración principal del proyecto
│   ├── settings.py                  # Configuración central (BD, seguridad, apps)
│   ├── urls.py                      # Enrutamiento principal
│   └── wsgi.py                      # Punto de entrada WSGI
│
├── usuarios/                        # App: Gestión de usuarios
│   ├── models.py                    # Modelos: Usuario, Rol
│   ├── views.py                     # Vistas: Login, Registro, Lista, Perfil, Roles
│   ├── forms.py                     # Formularios de registro y actualización
│   ├── signals.py                   # Señales: login fallido, bloqueo de cuenta
│   └── urls.py                      # Rutas de usuarios
│
├── incidentes/                      # App: Gestión de incidentes
│   ├── models.py                    # Modelos: Incidente, Sector, TipoDelito, Testigo, OperativoPolicial
│   ├── views.py                     # Vistas: CRUD, mapa, validación
│   ├── forms.py                     # Validación de formularios e imágenes
│   └── urls.py                      # Rutas de incidentes + API JSON
│
├── auditoria/                       # App: Seguridad y auditoría
│   ├── models.py                    # Modelo: AuditLog
│   ├── middleware.py                # Middleware: CSP, ErrorBoundary, ThreadLocal
│   └── admin.py                     # Panel admin de auditoría
│
├── estadisticas/                    # App: Estadísticas y dashboard
│   └── models.py                    # Modelo: EstadisticaIncidente
│
├── predicciones/                    # App: Predicción con IA
│   └── models.py                    # Modelos: PrediccionZona, ModeloIA
│
├── alertas/                         # App: Sistema de alertas
│   └── models.py                    # Modelos: Alerta, SuscripcionAlerta
│
├── templates/                       # Plantillas HTML
│   ├── base.html                    # Layout principal con navbar y accesibilidad
│   ├── login.html                   # Página de inicio de sesión
│   ├── registro.html                # Página de registro público
│   ├── dashboard.html               # Panel principal post-login
│   ├── incidentes/
│   │   ├── lista.html               # Lista de incidentes con filtros
│   │   ├── crear.html               # Formulario de creación con mapa
│   │   ├── detalle.html             # Vista detallada del incidente
│   │   ├── mapa.html                # Mapa general de incidentes
│   │   └── bandeja_validacion.html  # Bandeja de validación para admins
│   └── usuarios/
│       ├── lista.html               # Lista de usuarios con gestión de roles
│       ├── crear.html               # Creación de usuarios (admin)
│       ├── cambiar_rol.html         # Cambio de rol/estado/barrio
│       └── perfil.html              # Perfil del usuario actual
│
├── static/
│   ├── css/
│   │   └── styles.css               # Estilos globales + diseño responsivo
│   └── js/
│       └── leaflet.js               # Versión local de Leaflet (respaldo)
│
└── media/                           # Archivos subidos (desarrollo local)
```

---

## 2. ESPECIFICACIÓN DE REQUISITOS

### 2.1 Requisitos Funcionales

#### Módulo de Autenticación y Usuarios

| ID | Requisito | Descripción | Prioridad |
|----|-----------|-------------|-----------|
| RF-01 | Registro de usuarios | Los ciudadanos pueden registrarse con nombre, email, contraseña y barrio/selección de sector | Alta |
| RF-02 | Inicio de sesión | Sistema de autenticación contra base de datos con protección anti fuerza bruta (10 intentos/15 min por IP) | Alta |
| RF-03 | Cierre de sesión | Logout seguro con invalidación de sesión y cookies | Alta |
| RF-04 | Perfil de usuario | Cada usuario puede ver y editar sus datos personales y cambiar contraseña | Media |
| RF-05 | Roles de usuario | Sistema de permisos: Vecino, Administrador de Junta Vecinal, Superadministrador | Alta |
| RF-06 | Gestión de roles | Superadmin y Admin de Junta pueden cambiar roles, estados y barrios de usuarios en su jurisdicción | Alta |
| RF-07 | Bloqueo automático | Después de 5 intentos fallidos de login, la cuenta se bloquea automáticamente | Media |
| RF-08 | Reportes falsos | Usuarios con 10+ reportes falsos son inhabilitados automáticamente | Media |

#### Módulo de Incidentes

| ID | Requisito | Descripción | Prioridad |
|----|-----------|-------------|-----------|
| RF-09 | Crear incidente | Formulario con: título, tipo de delito, sector, dirección, descripción, foto y coordenadas GPS | Alta |
| RF-10 | Geolocalización GPS | Captura automática de latitud/longitud mediante la API de geolocalización del navegador | Alta |
| RF-11 | Mapa interactivo | Visualización de todos los incidentes activos en Google Maps con marcadores coloreados por tipo | Alta |
| RF-12 | Selección manual de ubicación | Posibilidad de arrastrar marcador o hacer clic en el mapa para fijar coordenadas | Alta |
| RF-13 | Zoom a incidente | Desde la página de detalle, el botón "Ver en Mapa" hace zoom al incidente seleccionado | Alta |
| RF-14 | Evidencia fotográfica | Subida de imágenes (JPG, PNG, WebP) con validación PIL, límite 5MB, almacenamiento Cloudinary | Alta |
| RF-15 | Lista de incidentes | Vista tabular con filtros por sector, tipo de delito y fecha, con paginación | Alta |
| RF-16 | Detalle de incidente | Vista completa con: título, tipo, sector, coordenadas, descripción, foto, testigos asociados | Alta |
| RF-17 | Testigos | Los usuarios pueden aportar testimonios, comentarios y fotos adicionales a incidentes existentes | Media |
| RF-18 | Validación de incidentes | Admin de Junta y Superadmin validan incidentes como "validado" o "falso" | Alta |
| RF-19 | Detección de duplicados | El sistema detecta si se reporta un incidente idéntico a <50m de distancia en <10 minutos | Media |
| RF-20 | Reporte anónimo | Opción de reportar incidentes de forma anónima, ocultando el nombre del reportante | Media |
| RF-21 | API JSON de incidentes | Endpoint `/incidentes/api/mapa/` que devuelve datos geo en formato JSON para el mapa | Alta |

#### Módulo de Estadísticas y Predicciones

| ID | Requisito | Descripción | Prioridad |
|----|-----------|-------------|-----------|
| RF-22 | Dashboard de estadísticas | Panel con métricas: incidentes por sector, por tipo, por día, tendencias | Media |
| RF-23 | Predicciones IA | Modelo scikit-learn que predice probabilidad de incidentes por sector y tipo de delito | Media |
| RF-24 | Historial de modelos | Registro de entrenamientos del modelo IA con versión, precisión, fecha | Baja |

#### Módulo de Alertas

| ID | Requisito | Descripción | Prioridad |
|----|-----------|-------------|-----------|
| RF-25 | Sistema de alertas | Cada incidente validado genera alertas para usuarios suscritos a ese sector | Media |
| RF-26 | Suscripción por sector | Usuarios se suscriben a sectores específicos para recibir alertas | Media |
| RF-27 | Configuración de canales | Selección de canal preferido: WhatsApp, Telegram o ambos | Baja |

### 2.2 Requisitos No Funcionales

#### Seguridad (RNF-S)

| ID | Requisito | Descripción |
|----|-----------|-------------|
| RNF-S01 | Content Security Policy (CSP) | Política restrictiva de orígenes de recursos: default-src 'self', frame-src 'none', form-action 'self' |
| RNF-S02 | HTTPS forzado | Redirección automática de HTTP a HTTPS mediante SECURE_SSL_REDIRECT |
| RNF-S03 | HSTS | HTTP Strict Transport Security configurado a 1 año con includeSubDomains y preload |
| RNF-S04 | Protección CSRF | Token CSRF en todos los formularios, cookies HTTPOnly, SameSite=Lax |
| RNF-S05 | XSS Protection | Header X-XSS-Protection activado, Content-Type nosniff, template auto-escaping |
| RNF-S06 | Clickjacking | X-Frame-Options: DENY + CSP frame-src: 'none' |
| RNF-S07 | Rate Limiting | Login: 10 intentos/15min por IP; Registro: 3/hora por IP; Incidentes: 10/hora por usuario |
| RNF-S08 | Password Hashing | Argon2 como hasher primario, PBKDF2 como respaldo |
| RNF-S09 | Cookies seguras | HTTPOnly, Secure (HTTPS), SameSite=Lax, SESSION_EXPIRE_AT_BROWSER_CLOSE |
| RNF-S10 | Validación de imágenes | PIL.verify() para verificar que el archivo es realmente una imagen, límite 5MB, tipos permitidos |
| RNF-S11 | Path traversal protection | La vista de media verifica que la ruta resuelta esté dentro de MEDIA_ROOT |
| RNF-S12 | Límites de upload | 10MB máximo por request, 5 archivos máximo, 200 campos máximo |
| RNF-S13 | Error handling | ErrorBoundaryMiddleware captura excepciones y retorna página genérica sin stack trace |
| RNF-S14 | Auditoría completa | AuditLog registra: login/logout exitoso y fallido, creación de incidentes, cambios de rol, validaciones |
| RNF-S15 | Referrer-Policy | same-origin: no se envía el header Referer a sitios externos |
| RNF-S16 | Gunicorn hardening | timeout 30s, keep-alive 2s, max-requests 2000 con jitter 200, 2 workers |

#### Rendimiento y Disponibilidad (RNF-R)

| ID | Requisito | Descripción |
|----|-----------|-------------|
| RNF-R01 | Connection pooling | CONN_MAX_AGE=600 (10 min), CONN_HEALTH_CHECKS=True |
| RNF-R02 | Servidor WSGI | Gunicorn con timeout 30s para prevenir slowloris |
| RNF-R03 | Reciclado de workers | max-requests 2000 para prevenir memory leaks |
| RNF-R04 | WhiteNoise | Archivos estáticos servidos con compresión y caché |

#### Usabilidad y Accesibilidad (RNF-U)

| ID | Requisito | Descripción |
|----|-----------|-------------|
| RNF-U01 | Diseño responsivo | Adaptación a móvil, tablet y desktop con Bootstrap 5 + media queries |
| RNF-U02 | Texto grande | Botón de accesibilidad que escala el texto base de 1rem a 1.25rem |
| RNF-U03 | Modo adulto mayor | Botones más grandes, inputs más grandes, bordes más redondeados |
| RNF-U04 | Idioma español | Interfaz completamente en español, LANGUAGE_CODE='es', TIME_ZONE='America/La_Paz' |
| RNF-U05 | Tablas adaptativas | En móvil, las tablas se convierten a tarjetas con data-label para cada celda |
| RNF-U06 | Barra de accesibilidad | Barra superior fija con toggles de texto grande y modo adulto mayor |
| RNF-U07 | Animaciones sutiles | Fade-in en carga de páginas, micro-interacciones en botones y tarjetas |
| RNF-U08 | Scrollbar personalizado | Barras de desplazamiento estilizadas con colores del tema |

#### Despliegue (RNF-D)

| ID | Requisito | Descripción |
|----|-----------|-------------|
| RNF-D01 | Despliegue en Railway | Plataforma PaaS con deploy automático desde GitHub |
| RNF-D02 | Migraciones automáticas | `python manage.py migrate --noinput` en cada deploy |
| RNF-D03 | Almacenamiento externo | Cloudinary para imágenes (persistencia entre deploys) |
| RNF-D04 | Variables de entorno | Todas las credenciales en .env y variables de Railway (nunca en código) |
| RNF-D05 | Respaldo Git | Tag v1.0-estable como punto de restauración |

### 2.3 Actores del Sistema

| Actor | Descripción | Permisos |
|-------|-------------|----------|
| **Vecino** | Ciudadano registrado en la plataforma | Reportar incidentes, ver mapa y estadísticas, agregar testimonios, suscribirse a alertas |
| **Administrador de Junta Vecinal** | Representante de un barrio/sector | Todos los de Vecino + Validar incidentes de su sector + Gestionar roles de vecinos de su sector |
| **Superadministrador** | Administrador global del sistema | Acceso total: gestionar todos los usuarios, roles, validar cualquier incidente, crear usuarios |
| **Visitante no autenticado** | Usuario sin sesión | Solo puede ver la página de login y registro |

### 2.4 Diagrama de Casos de Uso

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      SANTA CRUZ SEGURA PREDICTIVA                       │
│                                                                         │
│  ┌─────────────┐         ┌──────────────────────────────────┐          │
│  │  Visitante   │────────▶│  Registrarse                     │          │
│  └─────────────┘         │  Iniciar sesión                  │          │
│                          └──────────────────────────────────┘          │
│                                                                         │
│  ┌─────────────┐         ┌──────────────────────────────────┐          │
│  │    Vecino    │────────▶│  Reportar incidente (GPS + foto)│          │
│  │             │         │  Ver mapa de incidentes          │          │
│  │             │         │  Filtrar incidentes              │          │
│  │             │         │  Ver detalle de incidente        │          │
│  │             │         │  Agregar testimonio              │          │
│  │             │         │  Ver estadísticas                │          │
│  │             │         │  Suscribirse a alertas           │          │
│  │             │         │  Ver predicciones IA             │          │
│  │             │         │  Gestionar perfil                │          │
│  └─────────────┘         └──────────────────────────────────┘          │
│                                                                         │
│  ┌─────────────┐         ┌──────────────────────────────────┐          │
│  │ Admin Junta  │────────▶│  (Todo lo de Vecino)            │          │
│  │   Vecinal    │         │  Validar/descartar incidentes    │          │
│  │             │         │    (solo de su sector)            │          │
│  │             │         │  Gestionar roles de vecinos      │          │
│  │             │         │    (solo de su sector)            │          │
│  └─────────────┘         └──────────────────────────────────┘          │
│                                                                         │
│  ┌─────────────┐         ┌──────────────────────────────────┐          │
│  │  Superadmin  │────────▶│  (Todo lo de Admin Junta)       │          │
│  │             │         │  Validar cualquier incidente     │          │
│  │             │         │  Gestionar roles de todos        │          │
│  │             │         │  Crear usuarios manualmente      │          │
│  │             │         │  Deshabilitar/bloquear usuarios   │          │
│  │             │         │  Acceso al panel Django Admin    │          │
│  └─────────────┘         └──────────────────────────────────┘          │
└─────────────────────────────────────────────────────────────────────────┘
```

### 2.5 Diagrama de Objetos

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         DIAGRAMA DE OBJETOS                             │
│                                                                         │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────────┐        │
│  │    Usuario    │────▶│    AuditLog   │     │ SuscripcionAlerta│        │
│  │──────────────│     │──────────────│     │──────────────────│        │
│  │ username      │     │ fecha         │     │ canal_preferido   │        │
│  │ email         │     │ accion        │     │ sector            │        │
│  │ password      │     │ modelo        │     │ usuario           │        │
│  │ rol (FK)      │     │ registro_id   │     │ recibir_predictivas│       │
│  │ estado        │     │ detalles      │     └────────┬─────────┘        │
│  │ telefono      │     │ ip_origen     │              │                  │
│  │ barrio (FK)   │     └──────────────┘              │                  │
│  │ intentos_fallidos│                                 │                  │
│  │ reportes_falsos  │                                 │                  │
│  └───────┬──────┘                                     │                  │
│          │                                            │                  │
│  ┌───────▼──────┐                                     │                  │
│  │     Rol      │                                     │                  │
│  │──────────────│                                     │                  │
│  │ nombre        │                                     │                  │
│  └──────────────┘                                     │                  │
│                                                        │                  │
│  ┌──────────────────┐                                 │                  │
│  │    Incidente     │                                 │                  │
│  │──────────────────│                                 │                  │
│  │ titulo           │     ┌──────────────┐            │                  │
│  │ descripcion      │────▶│   Testigo    │            │                  │
│  │ latitud          │     └──────────────┘            │                  │
│  │ longitud         │                                  │                  │
│  │ direccion        │     ┌──────────────────┐        │                  │
│  │ fecha_hora       │     │  PrediccionZona  │        │                  │
│  │ sector (FK)      │────▶│──────────────────│        │                  │
│  │ tipo (FK)        │     │ probabilidad      │        │                  │
│  │ reporte_por (FK) │     │ sector            │        │                  │
│  │ imagen           │     │ tipo              │        │                  │
│  │ estado           │     └──────────────────┘        │                  │
│  │ validador (FK)   │                                  │                  │
│  │ activo           │     ┌──────────────────┐        │                  │
│  │ reporte_anonimo  │     │     Alerta       │        │                  │
│  └──────────────────┘     │──────────────────│        │                  │
│                           │ incidente (FK)    │◀───────┘                  │
│  ┌──────────────┐        │ mensaje           │                           │
│  │  TipoDelito  │        │ fecha              │                           │
│  │──────────────│        │ leido              │                           │
│  │ nombre        │        └──────────────────┘                           │
│  └──────────────┘                                                        │
│                                                                          │
│  ┌──────────────┐        ┌──────────────────┐                           │
│  │    Sector    │        │    ModeloIA      │                           │
│  │──────────────│        │──────────────────│                           │
│  │ nombre        │        │ version           │                           │
│  │ centro_lat    │        │ precision_obtenida│                           │
│  │ centro_lon    │        │ registros_usados  │                           │
│  └──────────────┘        │ estado            │                           │
│                          │ ruta_archivo      │                           │
│  ┌──────────────┐        └──────────────────┘                           │
│  │Estadistica   │                                                       │
│  │Incidente     │                                                       │
│  │──────────────│                                                       │
│  │ nombre        │                                                       │
│  │ valor         │                                                       │
│  │ fecha         │                                                       │
│  └──────────────┘                                                       │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 3. DISEÑO DE BASE DE DATOS

### 3.1 Modelo Conceptual (Diagrama Entidad-Relación)

```
┌──────────┐       ┌──────────┐       ┌──────────┐       ┌──────────┐
│   Rol    │       │ Usuario  │       │  Sector  │       │TipoDelito│
│──────────│       │──────────│       │──────────│       │──────────│
│ id (PK)  │◀──┐   │ id (PK)  │   ┌──│ id (PK)  │       │ id (PK)  │
│ nombre   │   │   │ username │   │  │ nombre   │       │ nombre   │
└──────────┘   │   │ email    │   │  │centro_lat│       └──────────┘
               │   │ password │   │  │centro_lon│             │
               └───│ rol (FK) │   │  └──────────┘             │
                   │ barrio───┼───┘      ▲                     │
                   │ telefono │          │                     │
                   │ estado   │    ┌─────┴──────────┐          │
                   │ intentos_f│   │  Incidente     │          │
                   │ reportes_f│   │────────────────│          │
                   └──────────┘   │ id (PK)        │          │
                        │         │ titulo         │          │
                        │         │ descripcion    │          │
                        │   ┌─────│ sector (FK)    │──────────┘
          ┌─────────────┼───│─────│ tipo (FK)      │──────────┐
          │             │   │     │ latitud        │          │
          │             │   │     │ longitud       │    ┌─────┴──────────┐
    ┌─────┴──────┐      │   │     │ direccion      │    │ Operativo      │
    │ AuditLog   │      │   │     │ fecha_hora    │    │ Policial       │
    │────────────│      │   │     │ reporte_por───┼────│────────────────│
    │ id (PK)    │      │   │     │ imagen        │    │ id (PK)        │
    │ usuario────┼──────┘   │     │ estado        │    │ policia (FK)   │
    │ fecha      │          │     │ validador─────┤    │ sector (FK)    │
    │ accion     │          │     │ activo        │    │ fecha          │
    │ modelo     │          │     │reporte_anonimo│    │ num_agents     │
    │ registro_id│          │     │ num_testigos  │    │ zona_asignada  │
    │ detalles   │          │     └───────────────┘    └────────────────┘
    │ ip_origen  │          │           │
    └────────────┘          │     ┌─────┴──────────┐
                            │     │   Testigo      │
                            │     │────────────────│
┌──────────────────┐       │     │ id (PK)        │
│ PrediccionZona   │       │     │ incidente(FK)──┘
│──────────────────│       │     │ usuario (FK)
│ id (PK)          │       │     │ canal_origen
│ sector (FK)      │───────┘     │ comentario
│ tipo (FK)        │             │ imagen
│ probabilidad     │             │ fecha_reporte
└──────────────────┘             │reporte_anonimo
                                 └────────────────┘
┌──────────────────┐
│     Alerta       │       ┌────────────────────────┐
│──────────────────│       │ SuscripcionAlerta      │
│ id (PK)          │       │────────────────────────│
│ incidente (FK)───┘       │ id (PK)                │
│ mensaje                  │ usuario (FK)            │
│ fecha                    │ sector (FK)             │
│ leido                    │ canal_preferido         │
│ creado_por (FK)          │ recibir_predictivas     │
└──────────────────────────│ fecha_suscripcion       │
                           └────────────────────────┘

┌──────────────────┐       ┌──────────────────┐
│ ModeloIA         │       │EstadisticaIncidente│
│──────────────────│       │──────────────────│
│ id (PK)          │       │ id (PK)          │
│ version          │       │ nombre           │
│ precision        │       │ valor            │
│ registros_usados │       │ fecha            │
│ estado           │       └──────────────────┘
│ ruta_archivo     │
└──────────────────┘
```

### 3.2 Modelo Lógico (Tablas)

#### Tabla: `usuarios_rol`
| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id | INT(11) | PK, AUTO_INCREMENT | Identificador único |
| nombre | VARCHAR(50) | UNIQUE, NOT NULL | Nombre del rol (Vecino, Administrador de Junta, Superadministrador) |

#### Tabla: `usuarios_usuario`
| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id | INT(11) | PK, AUTO_INCREMENT | Identificador único |
| username | VARCHAR(150) | UNIQUE, NOT NULL | Nombre de usuario |
| email | VARCHAR(254) | NOT NULL | Correo electrónico |
| password | VARCHAR(128) | NOT NULL | Hash de contraseña (Argon2) |
| first_name | VARCHAR(150) | | Nombre real |
| last_name | VARCHAR(150) | | Apellido real |
| is_superuser | TINYINT(1) | DEFAULT 0 | Acceso total al sistema |
| is_staff | TINYINT(1) | DEFAULT 0 | Acceso al panel admin |
| is_active | TINYINT(1) | DEFAULT 1 | Cuenta activa (se sincroniza con estado) |
| date_joined | DATETIME | NOT NULL | Fecha de registro |
| rol_id | INT(11) | FK → usuarios_rol.id, ON DELETE SET NULL | Rol asignado |
| telefono | VARCHAR(20) | NULL | Número de teléfono |
| estado | VARCHAR(20) | DEFAULT 'activo', CHECK IN ('activo','inhabilitado','bloqueado') | Estado de la cuenta |
| intentos_fallidos | INT(11) | DEFAULT 0 | Contador de intentos fallidos de login |
| reportes_falsos_mes | INT(11) | DEFAULT 0 | Reportes marcados como falsos este mes |
| barrio_id | INT(11) | FK → incidentes_sector.id, ON DELETE SET NULL | Sector/barrio asignado |

#### Tabla: `incidentes_sector`
| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id | INT(11) | PK, AUTO_INCREMENT | Identificador único |
| nombre | VARCHAR(100) | UNIQUE, NOT NULL | Nombre del sector/barrio |
| centro_lat | DECIMAL(10,8) | NULL | Latitud del centro del sector |
| centro_lon | DECIMAL(10,8) | NULL | Longitud del centro del sector |

#### Tabla: `incidentes_tipodelito`
| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id | INT(11) | PK, AUTO_INCREMENT | Identificador único |
| nombre | VARCHAR(100) | UNIQUE, NOT NULL | Tipo de delito (Robo, Asalto, Hurto, etc.) |

#### Tabla: `incidentes_incidente`
| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id | INT(11) | PK, AUTO_INCREMENT | Identificador único |
| titulo | VARCHAR(150) | NOT NULL | Título del reporte |
| descripcion | LONGTEXT | NOT NULL | Descripción detallada |
| latitud | DECIMAL(10,7) | NOT NULL | Coordenada de latitud |
| longitud | DECIMAL(10,7) | NOT NULL | Coordenada de longitud |
| direccion | VARCHAR(255) | NOT NULL | Dirección aproximada |
| fecha_hora | DATETIME | AUTO_NOW_ADD | Fecha y hora del reporte |
| sector_id | INT(11) | FK → incidentes_sector.id, CASCADE | Sector del incidente |
| tipo_id | INT(11) | FK → incidentes_tipodelito.id, CASCADE | Tipo de delito |
| reporte_por_id | INT(11) | FK → usuarios_usuario.id, SET NULL | Usuario que reportó |
| imagen | VARCHAR(100) | NULL | Ruta de la imagen (Cloudinary en producción) |
| activo | TINYINT(1) | DEFAULT 1 | Registro activo/eliminado lógicamente |
| estado | VARCHAR(20) | DEFAULT 'pendiente', CHECK IN ('pendiente','validado','falso') | Estado de validación |
| validador_id | INT(11) | FK → usuarios_usuario.id, SET NULL | Administrador que validó |
| fecha_hora_validacion | DATETIME | NULL | Fecha de validación |
| num_testigos | INT(11) | DEFAULT 1 | Número de testigos |
| reporte_anonimo | TINYINT(1) | DEFAULT 0 | Reporte anónimo |

#### Tabla: `incidentes_testigo`
| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id | INT(11) | PK, AUTO_INCREMENT | Identificador único |
| incidente_id | INT(11) | FK → incidentes_incidente.id, CASCADE | Incidente asociado |
| usuario_id | INT(11) | FK → usuarios_usuario.id, SET NULL | Testigo |
| canal_origen | VARCHAR(20) | DEFAULT 'web' | Canal de origen |
| fecha_reporte | DATETIME | AUTO_NOW_ADD | Fecha del testimonio |
| comentario | LONGTEXT | NULL | Comentario del testigo |
| imagen | VARCHAR(100) | NULL | Imagen de evidencia |
| reporte_anonimo | TINYINT(1) | DEFAULT 0 | Testimonio anónimo |

#### Tabla: `incidentes_operativopolicial`
| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id | INT(11) | PK, AUTO_INCREMENT | Identificador único |
| policia_id | INT(11) | FK → usuarios_usuario.id, CASCADE | Policía asignado |
| sector_id | INT(11) | FK → incidentes_sector.id, CASCADE | Sector del operativo |
| fecha | DATE | NOT NULL | Fecha del operativo |
| hora_inicio | TIME | NULL | Hora de inicio |
| hora_fin | TIME | NULL | Hora de fin |
| num_agents | INT(11) | DEFAULT 1 | Número de agentes |
| zona_asignada | VARCHAR(200) | | Zona específica |
| notas | LONGTEXT | | Notas del operativo |
| fecha_registro | DATETIME | AUTO_NOW_ADD | Fecha de registro en el sistema |

#### Tabla: `auditoria_auditlog`
| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id | INT(11) | PK, AUTO_INCREMENT | Identificador único |
| usuario_id | INT(11) | FK → usuarios_usuario.id, SET NULL | Usuario que realizó la acción |
| fecha | DATETIME | AUTO_NOW_ADD | Fecha y hora de la acción |
| accion | VARCHAR(200) | NOT NULL | Descripción de la acción |
| modelo | VARCHAR(100) | NOT NULL | Modelo afectado |
| registro_id | INT(11) | NULL | ID del registro afectado |
| detalles | LONGTEXT | | Detalles adicionales |
| ip_origen | VARCHAR(45) | NULL | Dirección IP de origen |

#### Tabla: `alertas_alerta`
| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id | INT(11) | PK, AUTO_INCREMENT | Identificador único |
| incidente_id | INT(11) | FK → incidentes_incidente.id, CASCADE | Incidente que genera la alerta |
| mensaje | VARCHAR(250) | NOT NULL | Texto de la alerta |
| fecha | DATETIME | AUTO_NOW_ADD | Fecha de la alerta |
| leido | TINYINT(1) | DEFAULT 0 | Estado de lectura |
| creado_por_id | INT(11) | FK → usuarios_usuario.id, SET NULL | Quién creó la alerta |

#### Tabla: `alertas_suscripcionalerta`
| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id | INT(11) | PK, AUTO_INCREMENT | Identificador único |
| usuario_id | INT(11) | FK → usuarios_usuario.id, CASCADE | Usuario suscrito |
| sector_id | INT(11) | FK → incidentes_sector.id, CASCADE | Sector suscrito |
| canal_preferido | VARCHAR(20) | DEFAULT 'ambos', CHECK IN ('whatsapp','telegram','ambos') | Canal de notificación |
| recibir_predictivas | TINYINT(1) | DEFAULT 1 | Recibir alertas predictivas |
| fecha_suscripcion | DATETIME | AUTO_NOW_ADD | Fecha de suscripción |
| | | UNIQUE(usuario_id, sector_id) | Un usuario solo puede suscribirse una vez por sector |

#### Tabla: `predicciones_prediccionzona`
| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id | INT(11) | PK, AUTO_INCREMENT | Identificador único |
| sector_id | INT(11) | FK → incidentes_sector.id, CASCADE | Sector predicho |
| tipo_id | INT(11) | FK → incidentes_tipodelito.id, CASCADE | Tipo de delito predicho |
| probabilidad | FLOAT | NOT NULL | Probabilidad (0.00-1.00) |
| fecha | DATETIME | AUTO_NOW_ADD | Fecha de la predicción |

#### Tabla: `predicciones_modeloia`
| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id | INT(11) | PK, AUTO_INCREMENT | Identificador único |
| version | VARCHAR(50) | NOT NULL | Versión del modelo |
| fecha_entrenamiento | DATETIME | AUTO_NOW_ADD | Fecha de entrenamiento |
| precision_obtenida | DECIMAL(5,2) | NULL | Precisión del modelo (0-100%) |
| registros_usados | INT(11) | DEFAULT 0 | Cantidad de registros usados |
| estado | VARCHAR(20) | CHECK IN ('activo','inactivo','descartado') | Estado del modelo |
| ruta_archivo | VARCHAR(255) | | Ruta del archivo del modelo |

#### Tabla: `estadisticas_estadistica`
| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id | INT(11) | PK, AUTO_INCREMENT | Identificador único |
| nombre | VARCHAR(100) | NOT NULL | Nombre de la métrica |
| valor | FLOAT | NOT NULL | Valor numérico |
| fecha | DATE | AUTO_NOW_ADD | Fecha de la estadística |

### 3.3 Modelo Físico (Script SQL)

```sql
-- Creación de base de datos
CREATE DATABASE IF NOT EXISTS santa_cruz_segura
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE santa_cruz_segura;

-- Tabla: Rol
CREATE TABLE usuarios_rol (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
) ENGINE=InnoDB;

-- Tabla: Sector
CREATE TABLE incidentes_sector (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    centro_lat DECIMAL(10,8) NULL,
    centro_lon DECIMAL(10,8) NULL
) ENGINE=InnoDB;

-- Tabla: TipoDelito
CREATE TABLE incidentes_tipodelito (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE
) ENGINE=InnoDB;

-- Tabla: Usuario
CREATE TABLE usuarios_usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(150) NOT NULL UNIQUE,
    email VARCHAR(254) NOT NULL,
    password VARCHAR(128) NOT NULL,
    first_name VARCHAR(150) NOT NULL DEFAULT '',
    last_name VARCHAR(150) NOT NULL DEFAULT '',
    is_superuser TINYINT(1) NOT NULL DEFAULT 0,
    is_staff TINYINT(1) NOT NULL DEFAULT 0,
    is_active TINYINT(1) NOT NULL DEFAULT 1,
    date_joined DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    rol_id INT NULL,
    telefono VARCHAR(20) NULL,
    estado VARCHAR(20) NOT NULL DEFAULT 'activo',
    intentos_fallidos INT NOT NULL DEFAULT 0,
    reportes_falsos_mes INT NOT NULL DEFAULT 0,
    barrio_id INT NULL,
    FOREIGN KEY (rol_id) REFERENCES usuarios_rol(id) ON DELETE SET NULL,
    FOREIGN KEY (barrio_id) REFERENCES incidentes_sector(id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- Tabla: Incidente
CREATE TABLE incidentes_incidente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    descripcion LONGTEXT NOT NULL,
    latitud DECIMAL(10,7) NOT NULL,
    longitud DECIMAL(10,7) NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    fecha_hora DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    sector_id INT NOT NULL,
    tipo_id INT NOT NULL,
    reporte_por_id INT NULL,
    imagen VARCHAR(100) NULL,
    activo TINYINT(1) NOT NULL DEFAULT 1,
    estado VARCHAR(20) NOT NULL DEFAULT 'pendiente',
    validador_id INT NULL,
    fecha_hora_validacion DATETIME NULL,
    num_testigos INT NOT NULL DEFAULT 1,
    reporte_anonimo TINYINT(1) NOT NULL DEFAULT 0,
    FOREIGN KEY (sector_id) REFERENCES incidentes_sector(id) ON DELETE CASCADE,
    FOREIGN KEY (tipo_id) REFERENCES incidentes_tipodelito(id) ON DELETE CASCADE,
    FOREIGN KEY (reporte_por_id) REFERENCES usuarios_usuario(id) ON DELETE SET NULL,
    FOREIGN KEY (validador_id) REFERENCES usuarios_usuario(id) ON DELETE SET NULL,
    INDEX idx_incidente_fecha (fecha_hora),
    INDEX idx_incidente_sector (sector_id),
    INDEX idx_incidente_estado (estado)
) ENGINE=InnoDB;

-- Tabla: Testigo
CREATE TABLE incidentes_testigo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    incidente_id INT NOT NULL,
    usuario_id INT NULL,
    canal_origen VARCHAR(20) NOT NULL DEFAULT 'web',
    fecha_reporte DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    comentario LONGTEXT NULL,
    imagen VARCHAR(100) NULL,
    reporte_anonimo TINYINT(1) NOT NULL DEFAULT 0,
    FOREIGN KEY (incidente_id) REFERENCES incidentes_incidente(id) ON DELETE CASCADE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios_usuario(id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- Tabla: AuditLog
CREATE TABLE auditoria_auditlog (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NULL,
    fecha DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    accion VARCHAR(200) NOT NULL,
    modelo VARCHAR(100) NOT NULL,
    registro_id INT NULL,
    detalles LONGTEXT NULL,
    ip_origen VARCHAR(45) NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios_usuario(id) ON DELETE SET NULL,
    INDEX idx_audit_fecha (fecha),
    INDEX idx_audit_accion (accion),
    INDEX idx_audit_ip (ip_origen)
) ENGINE=InnoDB;

-- Tabla: Alerta
CREATE TABLE alertas_alerta (
    id INT AUTO_INCREMENT PRIMARY KEY,
    incidente_id INT NOT NULL,
    mensaje VARCHAR(250) NOT NULL,
    fecha DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    leido TINYINT(1) NOT NULL DEFAULT 0,
    creado_por_id INT NULL,
    FOREIGN KEY (incidente_id) REFERENCES incidentes_incidente(id) ON DELETE CASCADE,
    FOREIGN KEY (creado_por_id) REFERENCES usuarios_usuario(id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- Tabla: SuscripcionAlerta
CREATE TABLE alertas_suscripcionalerta (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    sector_id INT NOT NULL,
    canal_preferido VARCHAR(20) NOT NULL DEFAULT 'ambos',
    recibir_predictivas TINYINT(1) NOT NULL DEFAULT 1,
    fecha_suscripcion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios_usuario(id) ON DELETE CASCADE,
    FOREIGN KEY (sector_id) REFERENCES incidentes_sector(id) ON DELETE CASCADE,
    UNIQUE KEY uniq_usuario_sector (usuario_id, sector_id)
) ENGINE=InnoDB;

-- Tabla: PrediccionZona
CREATE TABLE predicciones_prediccionzona (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sector_id INT NOT NULL,
    tipo_id INT NOT NULL,
    probabilidad FLOAT NOT NULL,
    fecha DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sector_id) REFERENCES incidentes_sector(id) ON DELETE CASCADE,
    FOREIGN KEY (tipo_id) REFERENCES incidentes_tipodelito(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Tabla: ModeloIA
CREATE TABLE predicciones_modeloia (
    id INT AUTO_INCREMENT PRIMARY KEY,
    version VARCHAR(50) NOT NULL,
    fecha_entrenamiento DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    precision_obtenida DECIMAL(5,2) NULL,
    registros_usados INT NOT NULL DEFAULT 0,
    estado VARCHAR(20) NOT NULL DEFAULT 'activo',
    ruta_archivo VARCHAR(255) NOT NULL DEFAULT ''
) ENGINE=InnoDB;

-- Tabla: EstadisticaIncidente
CREATE TABLE estadisticas_estadisticaincidente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    valor FLOAT NOT NULL,
    fecha DATE NOT NULL DEFAULT (CURRENT_DATE)
) ENGINE=InnoDB;

-- Datos semilla
INSERT INTO usuarios_rol (nombre) VALUES
    ('Vecino'),
    ('Administrador de Junta'),
    ('Superadministrador');

INSERT INTO incidentes_tipodelito (nombre) VALUES
    ('Robo'),
    ('Asalto'),
    ('Hurto'),
    ('Vandalismo'),
    ('Agresion'),
    ('Secuestro'),
    ('Narcotrafico'),
    ('Homicidio'),
    ('Violencia domestica'),
    ('Acoso callejero'),
    ('Extorsion'),
    ('Otro');

INSERT INTO incidentes_sector (nombre, centro_lat, centro_lon) VALUES
    ('Centro', -17.7833, -63.1821),
    ('Norte', -17.7500, -63.1500),
    ('Sur', -17.8200, -63.2000),
    ('Este', -17.7700, -63.1200),
    ('Oeste', -17.7900, -63.2200),
    ('Equipetrol', -17.7600, -63.1600),
    ('Plan 3.000', -17.8000, -63.1700),
    ('Palmar del Oratorio', -17.7400, -63.1400),
    ('Pirai', -17.7600, -63.1900),
    ('Urubo', -17.7200, -63.1300);
```

---

## 4. PLANIFICACIÓN DEL DESARROLLO

### 4.1 Metodología Seleccionada (SCRUM)

Se adoptó la metodología **SCRUM** por las siguientes razones:

- **Desarrollo iterativo e incremental**: El sistema se construyó en sprints de 1-2 semanas, permitiendo entregas funcionales después de cada iteración
- **Adaptabilidad**: Los requisitos evolucionaron durante el desarrollo (ej. cambio de tiles de mapa de OpenStreetMap a Google Maps, integración de Cloudinary)
- **Retroalimentación continua**: Las pruebas con usuarios reales revelaron problemas (marcadores invisibles, errores de localización, imágenes perdidas) que se corrigieron en sprints posteriores

**Roles SCRUM:**
| Rol | Responsable | Persona |
|-----|-------------|---------|
| Product Owner | Definir prioridades y requisitos | Docente/Cliente |
| Scrum Master | Facilitar el proceso y eliminar bloqueos | Desarrollador |
| Development Team | Implementar funcionalidades | Equipo de desarrollo |

#### Diagrama de Gantt

```
Sprint  | SEM 1 | SEM 2 | SEM 3 | SEM 4 | SEM 5 | SEM 6 | SEM 7 | SEM 8 |
────────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
Sprint 1| ████████████████ │       │       │       │       │       │       │  Setup + Auth
Sprint 2|       │ ████████████████ │       │       │       │       │       │  Incidentes CRUD
Sprint 3|       │       │ ████████████████ │       │       │       │       │  Mapa + Geoloc
Sprint 4|       │       │       │ ████████████████ │       │       │       │  Validación
Sprint 5|       │       │       │       │ ████████████████ │       │       │  Seguridad
Sprint 6|       │       │       │       │       │ ████████████████ │       │  Estadísticas
Sprint 7|       │       │       │       │       │       │ ████████████████ │  IA + Alertas
Sprint 8|       │       │       │       │       │       │       │ ████████████████│  Pruebas/Deploy
────────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
Revisión│   ✓   │   ✓   │   ✓   │   ✓   │   ✓   │   ✓   │   ✓   │   ✓   │
```

### 4.2 Objetivos SMART

| Objetivo | Específico | Medible | Alcanzable | Relevante | Temporal |
|----------|-----------|---------|------------|-----------|----------|
| **O1** | Sistema de autenticación con 3 roles diferenciados | 100% de usuarios con rol asignado, 3 vistas protegidas por rol | Con Django Auth + modelo Rol personalizado | Esencial para la seguridad del sistema | Sprint 1 (2 semanas) |
| **O2** | Mapa interactivo con marcadores por tipo de delito | Renderizar 26+ incidentes con marcadores coloreados y popups informativos | Leaflet.js + API JSON + Google Maps tiles | Funcionalidad central del MVP | Sprint 3 (2 semanas) |
| **O3** | Reporte de incidente con GPS y foto en < 30 segundos | Prueba: completar formulario en 25s promedio en móvil | Geolocation API + Cloudinary upload | Usabilidad móvil crucial | Sprint 3 (2 semanas) |
| **O4** | Validación comunitaria con 3 testigos mínimo | Auto-validación al alcanzar 3 testigos | Signals + contador de testigos | Fomenta participación | Sprint 4 (2 semanas) |
| **O5** | 92+ medidas de seguridad implementadas | 0 vulnerabilidades críticas en auditoría OWASP | Django security features + middleware personalizados | Protección de datos ciudadanos | Sprint 5 (2 semanas) |

### 4.3 Herramientas de Desarrollo

| Herramienta | Versión | Uso |
|-------------|---------|-----|
| Visual Studio Code | 1.95+ | Editor de código |
| Python | 3.12+ | Lenguaje de programación |
| Django | 5.2 | Framework web |
| Git | 2.47+ | Control de versiones |
| GitHub | — | Repositorio remoto y CI/CD |
| Railway | — | Plataforma de despliegue (PaaS) |
| MySQL Workbench | 8.0 | Administración de base de datos |
| Cloudinary | — | Almacenamiento cloud de imágenes |
| Google Chrome DevTools | — | Depuración frontend, consola, red |
| scikit-learn | 1.4 | Machine learning para predicciones |
| pandas | 2.0 | Análisis de datos |
| Pillow | 10.0 | Validación de imágenes |
| Bootstrap 5 | 5.3 | Framework CSS responsivo |
| Leaflet.js | 1.9.4 | Biblioteca de mapas interactivos |

### 4.4 Matriz RACI

| Actividad | Desarrollador | Product Owner | Docente |
|-----------|---------------|---------------|---------|
| Definición de requisitos | C | R | A |
| Diseño de base de datos | R | C | I |
| Implementación de modelos | R | I | I |
| Desarrollo de vistas y lógica | R | C | I |
| Diseño de interfaz de usuario | R | C | A |
| Integración de mapa Leaflet | R | I | I |
| Implementación de seguridad | R | C | A |
| Pruebas unitarias y de integración | R | C | A |
| Despliegue en Railway | R | I | I |
| Documentación del proyecto | R | A | I |
| Defensa oral del proyecto | R | I | A |

**Leyenda**: R = Responsible (Ejecuta), A = Accountable (Aprueba), C = Consulted (Consulta), I = Informed (Informado)

### 4.5 Estimación de Tiempos

| Sprint | Historias de usuario | Horas estimadas | Horas reales |
|--------|---------------------|-----------------|--------------|
| Sprint 1: Setup + Auth + Modelos | 5 | 24h | 21h |
| Sprint 2: Incidentes CRUD | 6 | 28h | 32h |
| Sprint 3: Mapa + Geolocalización + Fotos | 8 | 36h | 44h (problemas con CDN, tiles, marcadores) |
| Sprint 4: Validación + Testigos | 4 | 18h | 15h |
| Sprint 5: Seguridad (CSP, HSTS, rate limiting) | 7 | 30h | 28h |
| Sprint 6: Estadísticas + Dashboard | 3 | 12h | 10h |
| Sprint 7: Predicciones IA + Alertas | 5 | 20h | 18h |
| Sprint 8: Pruebas + Despliegue + Documentación | 6 | 24h | 30h |
| **TOTAL** | **44 historias** | **192h** | **198h** |

### 4.6 Alcance (MVP y MoSCoW)

#### Must Have (Debe tener) — MVP

| Funcionalidad | Estado |
|---------------|--------|
| Registro y autenticación de usuarios | ✅ Implementado |
| CRUD de incidentes con geolocalización | ✅ Implementado |
| Mapa interactivo con marcadores | ✅ Implementado |
| Subida de imágenes con validación | ✅ Implementado |
| Roles y permisos (3 niveles) | ✅ Implementado |
| Validación de incidentes | ✅ Implementado |
| Protección anti fuerza bruta | ✅ Implementado |
| CSP, HSTS, SSL enforce | ✅ Implementado |
| Diseño responsivo móvil | ✅ Implementado |
| Rate limiting (login, registro, incidentes) | ✅ Implementado |

#### Should Have (Debería tener)

| Funcionalidad | Estado |
|---------------|--------|
| Sistema de testigos | ✅ Implementado |
| Estadísticas y dashboard | ✅ Implementado |
| Predicciones con IA (scikit-learn) | ✅ Implementado |
| Alertas y suscripciones | ✅ Implementado |
| Almacenamiento cloud de imágenes (Cloudinary) | ✅ Implementado |
| API JSON para mapa | ✅ Implementado |

#### Could Have (Podría tener)

| Funcionalidad | Estado |
|---------------|--------|
| Modo oscuro | ❌ No implementado |
| Notificaciones push | ❌ No implementado |
| Exportación de reportes PDF | ✅ Implementado (reportlab) |
| Mapa de calor | ❌ Eliminado (incompatibilidad leaflet.heat) |
| CAPTCHA | ❌ No implementado |
| 2FA | ❌ No implementado |

#### Won't Have (No tendrá — esta versión)

| Funcionalidad | Razón |
|---------------|-------|
| Aplicación móvil nativa | Fuera de alcance, la app es PWA-ready |
| Integración con cámaras municipales | Sin acceso a API externa |
| Reconocimiento facial | Complejidad y privacidad |
| Pasarela de pagos | No requerida |

### 4.7 Plan de Contingencias

| Riesgo | Probabilidad | Impacto | Mitigación | Estado |
|--------|-------------|---------|------------|--------|
| **CDN de Leaflet bloqueado** | Alta | Alto | Se descargó Leaflet localmente en `/static/`. Se revirtió a CDN jsDelivr (mismo que Bootstrap). Plan C: Google Maps embebido | Mitigado |
| **Tiles de mapa no cargan** | Alta | Alto | Se probaron 4 proveedores (Google, OSM, CartoDB). Google Maps resultó el único funcional en Railway/Bolivia. CSP actualizado para mt1.google.com | Mitigado |
| **Marcadores invisibles por localización (coma decimal)** | Media | Alto | Se cambió `|floatformat:-7` por `{% localize off %}` en templates. Las URLs ahora usan punto decimal siempre | Mitigado |
| **Pérdida de imágenes en redeploy** | Alta | Medio | Integración con Cloudinary (almacenamiento externo persistente). Imágenes viejas perdidas, nuevas a salvo | Mitigado |
| **Ataque de fuerza bruta al login** | Alta | Medio | Rate limit 10 intentos/15 min por IP + bloqueo de cuenta a los 5 fallos. HTTP 429 con Retry-After | Mitigado |
| **Error 500 en producción** | Media | Medio | ErrorBoundaryMiddleware captura excepciones, registra en logs, muestra página genérica sin stack trace | Mitigado |
| **Caída de Railway** | Baja | Alto | Código en GitHub como respaldo. Se puede redeploy en otra plataforma (Render, Fly.io) en <1h | Aceptado |
| **Caída de MySQL en Railway** | Baja | Alto | CONN_HEALTH_CHECKS + CONN_MAX_AGE. Migraciones automáticas en cada deploy. Backup DB disponible | Mitigado |

### 4.8 Cronograma de Sprints

```
┌──────────────────────────────────────────────────────────────────────────┐
│                        CRONOGRAMA DE SPRINTS                             │
│                                                                          │
│  Sprint 1: Fundación (Semanas 1-2)                                      │
│    □ Setup del proyecto Django                                           │
│    □ Modelos: Usuario, Rol, Sector, TipoDelito, Incidente               │
│    □ Sistema de autenticación (login, registro, logout)                  │
│    □ Roles y permisos básicos                                            │
│    □ Templates base + Bootstrap + CSS                                    │
│                                                                          │
│  Sprint 2: Incidentes (Semanas 3-4)                                     │
│    □ CRUD completo de incidentes                                         │
│    □ Formulario con crispy_forms                                         │
│    □ Lista con filtros y paginación                                      │
│    □ Detalle con toda la metadata                                        │
│    □ Upload de imágenes con validación PIL                               │
│                                                                          │
│  Sprint 3: Mapa y Geolocalización (Semanas 5-6)                         │
│    □ Integración de Leaflet.js                                           │
│    □ API JSON para datos del mapa                                        │
│    □ Geolocalización GPS del navegador                                   │
│    □ Marcadores coloreados por tipo                                      │
│    □ Zoom a incidente desde detalle                                      │
│    □ Selección manual de ubicación en mapa                               │
│                                                                          │
│  Sprint 4: Validación y Comunidad (Semanas 7-8)                         │
│    □ Flujo de validación: pendiente → validado/falso                    │
│    □ Sistema de testigos                                                 │
│    □ Bloqueo por reportes falsos                                         │
│    □ Bandeja de validación para admins                                   │
│                                                                          │
│  Sprint 5: Seguridad (Semanas 9-10)                                     │
│    □ CSP Middleware                                                      │
│    □ Rate limiting en login, registro, incidentes                        │
│    □ HSTS, SSL Redirect, Secure cookies                                  │
│    □ ErrorBoundaryMiddleware                                             │
│    □ AuditLog para todas las acciones sensibles                          │
│    □ Argon2 password hashing                                             │
│    □ Gunicorn hardening                                                  │
│                                                                          │
│  Sprint 6: Estadísticas (Semanas 11-12)                                 │
│    □ Dashboard de estadísticas                                           │
│    □ Métricas por sector, tipo, tiempo                                   │
│    □ Exportación PDF con reportlab                                       │
│                                                                          │
│  Sprint 7: IA y Alertas (Semanas 13-14)                                 │
│    □ Modelo scikit-learn para predicciones                               │
│    □ Predicción por sector y tipo de delito                              │
│    □ Sistema de alertas                                                  │
│    □ Suscripciones por sector                                            │
│                                                                          │
│  Sprint 8: Despliegue y Pruebas (Semanas 15-16)                         │
│    □ Configuración de Railway                                            │
│    □ Whitenoise para estáticos                                           │
│    □ Cloudinary para imágenes                                            │
│    □ Pruebas de aceptación                                               │
│    □ Corrección de bugs post-deploy                                      │
│    □ Documentación completa                                              │
│    □ Tag de versión estable v1.0                                         │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 5. DESARROLLO TÉCNICO

### 5.1 Configuración de Ambientes

#### Ambiente de Desarrollo (Local)

- **Sistema operativo**: Windows 10/11 o Linux
- **Python**: 3.12+
- **Dependencias**: Todas listadas en `requirements.txt`
- **Base de datos**: MySQL local (opcional: SQLite para pruebas rápidas)
- **Variables de entorno**: Archivo `.env` en la raíz del proyecto
- **Servidor**: `python manage.py runserver`

```bash
# Instalación local
git clone https://github.com/SrHeath/SantaCruzSegura.git
cd santa_cruz_segura
pip install -r requirements.txt
cp .env.example .env
# Editar .env con credenciales locales
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

#### Ambiente de Producción (Railway)

- **Plataforma**: Railway.app (PaaS)
- **Servidor WSGI**: Gunicorn con 2 workers, timeout 30s, max-requests 2000
- **Base de datos**: MySQL provisto por Railway
- **Estáticos**: WhiteNoise con `WHITENOISE_USE_FINDERS = True`
- **Imágenes**: Cloudinary (`django-cloudinary-storage`)
- **URL**: `https://web-production-xxxx.up.railway.app`
- **Deploy**: Automático desde GitHub (push a `main`)

**Archivos clave de despliegue:**

`Procfile`:
```
web: gunicorn santa_cruz_segura.wsgi --timeout 30 --keep-alive 2 --workers 2 --max-requests 2000 --max-requests-jitter 200
```

`runtime.txt`:
```
python-3.12.0
```

**Variables de entorno en Railway:**
| Variable | Propósito |
|----------|-----------|
| `DJANGO_SECRET_KEY` | Clave criptográfica de Django |
| `DJANGO_DEBUG` | Modo debug (False en producción) |
| `DJANGO_ALLOWED_HOSTS` | Dominios permitidos (.up.railway.app) |
| `MYSQLHOST`, `MYSQLDATABASE`, `MYSQLUSER`, `MYSQLPASSWORD`, `MYSQLPORT` | Conexión MySQL |
| `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET` | Almacenamiento de imágenes |
| `DJANGO_CSRF_TRUSTED_ORIGINS` | Orígenes confiables para CSRF |
| `DJANGO_REGISTRATION_OPEN` | Control de apertura de registros |

### 5.2 Conexión a Base de Datos

**Configuración en `settings.py`:**

```python
if os.environ.get('MYSQLHOST'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['MYSQLDATABASE'],
            'USER': os.environ['MYSQLUSER'],
            'PASSWORD': os.environ.get('MYSQLPASSWORD', ''),
            'HOST': os.environ['MYSQLHOST'],
            'PORT': os.environ.get('MYSQLPORT', '3306'),
            'OPTIONS': {
                'charset': 'utf8mb4',
            },
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('DB_NAME', 'santa_cruz_segura'),
            'USER': os.environ.get('DB_USER', 'santacruz'),
            'PASSWORD': os.environ.get('DB_PASSWORD', ''),
            'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
            'PORT': os.environ.get('DB_PORT', '3306'),
            'OPTIONS': {
                'charset': 'utf8mb4',
            },
        }
    }
```

**Características de la conexión:**

- **Charset**: `utf8mb4` para soporte completo de Unicode (emojis, caracteres especiales del español como ñ, acentos)
- **Motor**: MySQL con `mysqlclient` como driver (rendimiento superior a PyMySQL)
- **Connection pooling**: `CONN_MAX_AGE = 600` (10 minutos de persistencia de conexiones)
- **Health checks**: `CONN_HEALTH_CHECKS = True` (verifica que la conexión siga viva antes de usarla)
- **Migraciones**: `python manage.py migrate --noinput` se ejecuta en cada deploy de Railway

**Servicios Railway (producción):**

Railway provee MySQL interno con red privada. Durante el pre-deploy, se usa un proxy público. Las variables de entorno son inyectadas automáticamente por Railway en cada contenedor.

### 5.3 Implementación de CRUD

El proyecto implementa operaciones CRUD completas para todas las entidades principales:

#### Incidentes

| Operación | URL | View | Método HTTP | Autenticación |
|-----------|-----|------|-------------|---------------|
| **Listar** | `/incidentes/` | `IncidenteListView` | GET | LoginRequired |
| **Crear** | `/incidentes/crear/` | `IncidenteCrearView` | GET/POST | LoginRequired + Rate limit 10/hora |
| **Leer** | `/incidentes/detalle/<pk>/` | `IncidenteDetalleView` | GET | LoginRequired |
| **Validar** | `/incidentes/validar/<pk>/<accion>/` | `IncidenteValidarAccionView` | POST | Admin/Superadmin |

**Características del CRUD de Incidentes:**

1. **Filtros en listado**: Por sector, tipo de delito, fecha. GPS automático para sugerir el sector más cercano
2. **Validación anti-spam**: Límite de 10 reportes/hora por usuario
3. **Detección de duplicados**: Distancia Haversine < 50 metros en < 10 minutos = rechazo
4. **Creación con mapa**: GPS automático + arrastre manual del marcador + clic en mapa
5. **Validación PIL**: Cada imagen se verifica byte a byte que sea JPEG/PNG/WebP real
6. **Cloudinary**: En producción, las imágenes se suben a Cloudinary y persisten entre deploys
7. **Soft delete**: Campo `activo=False` en vez de eliminación física

#### Usuarios

| Operación | URL | View | Permiso |
|-----------|-----|------|---------|
| **Listar** | `/usuarios/` | `UsuarioListView` | Superadmin + Admin de Junta |
| **Crear** | `/usuarios/crear/` | `UsuarioCrearView` | Solo Superadmin |
| **Editar rol** | `/usuarios/<pk>/rol/` | `UsuarioRolUpdateView` | Superadmin (todos) + Admin Junta (solo su sector) |
| **Editar perfil** | `/perfil/` | `PerfilView` | El usuario mismo |

**Control de acceso en `UsuarioRolUpdateView`:**

```python
def test_func(self):
    user = self.request.user
    if user.is_superuser:
        return True
    rol = getattr(user, 'rol', None)
    if not rol:
        return False
    if rol.nombre == 'Superadministrador':
        return True
    if rol.nombre == 'Administrador de Junta':
        target = self.get_object()
        return user.barrio and target.barrio == user.barrio
    return False
```

### 5.4 Diseño de Interfaces de Usuario

#### Sistema de Diseño

| Elemento | Especificación |
|----------|---------------|
| **Tipografía** | Outfit (títulos) + Inter (cuerpo) desde Google Fonts |
| **Paleta de colores** | Fondo: `#f1f5f9` (slate-100), Primario: `#1d4ed8` (blue-700), Navbar: `#0f172a` (slate-900) |
| **Tarjetas** | Glassmorphism con `backdrop-filter: blur(12px)` y sombras suaves |
| **Botones** | Efecto ripple en click, gradiente en hover, bordes `10px` |
| **Animaciones** | Fade-in en carga de página, hover con `translateY(-4px)` en tarjetas |
| **Scrollbar** | Personalizada (8px, slate-300) |

#### Páginas principales

1. **Login**: Formulario centrado con diseño glassmorphism, campos con iconos
2. **Registro**: Formulario público con campos: usuario, nombre, email, contraseña (2 veces), sector
3. **Dashboard**: Tarjetas resumen post-login
4. **Lista de incidentes**: Tabla con filtros, paginación, adaptación a tarjetas en móvil
5. **Crear incidente**: Panel dividido: mapa (izquierda) + formulario (derecha). GPS activo con barra de estado
6. **Detalle de incidente**: Metadata en cards, descripción, coordenadas con link al mapa, evidencia fotográfica, testimonios
7. **Mapa**: Ocupa pantalla completa con Google Maps tiles, circleMarkers coloreados, popups con info + foto
8. **Gestión de usuarios**: Tabla con roles, reportes falsos, estado. Botón "Rol" por cada usuario
9. **Cambiar rol**: Panel con info del usuario + formulario crispy para cambiar rol, estado y sector

#### Responsive Design

```css
/* Móvil (<576px) */
- Tablas → tarjetas apiladas con data-label
- Mapa altura 280px
- Botones full-width
- Navbar colapsable

/* Tablet (576px-768px) */
- Mapa altura 350px
- 2 columnas en lugar de 4
- Cards padding reducido

/* Desktop (>768px) */
- Mapa altura 650px
- Layout completo de columnas
- Glassmorphism full
```

### 5.5 Integración de IA Predictiva

El módulo de predicciones utiliza **scikit-learn** para entrenar un modelo de clasificación que estima la probabilidad de ocurrencia de cada tipo de delito por sector geográfico.

#### Proceso de IA

```
┌──────────────┐    ┌───────────────┐    ┌──────────────────┐
│  Datos        │───▶│ Preprocesamiento│───▶│  Entrenamiento  │
│  Históricos   │    │ (pandas)       │    │  (scikit-learn)  │
│  (Incidentes) │    └───────────────┘    └────────┬─────────┘
└──────────────┘                                      │
                                                      ▼
┌──────────────────┐                       ┌──────────────────┐
│  Predicciones    │◀──────────────────────│  Modelo           │
│  Zona x Tipo     │                       │  (RandomForest /  │
│  (PrediccionZona)│                       │   LogisticReg)    │
└──────────────────┘                       └──────────────────┘
```

#### Modelo de datos de IA

```python
class PrediccionZona(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoDelito, on_delete=models.CASCADE)
    probabilidad = models.FloatField()  # 0.00 a 1.00
    fecha = models.DateTimeField(auto_now_add=True)

class ModeloIA(models.Model):
    version = models.CharField(max_length=50)
    fecha_entrenamiento = models.DateTimeField(auto_now_add=True)
    precision_obtenida = models.DecimalField(max_digits=5, decimal_places=2)  # 0-100%
    registros_usados = models.IntegerField(default=0)
    estado = models.CharField(max_length=20)  # activo, inactivo, descartado
    ruta_archivo = models.CharField(max_length=255)
```

#### Features del modelo

| Feature | Tipo | Descripción |
|---------|------|-------------|
| `sector_id` | Categórica | Sector/barrio |
| `hora_del_dia` | Numérica | Hora del incidente (0-23) |
| `dia_semana` | Categórica | Lunes a Domingo |
| `mes` | Categórica | Enero a Diciembre |
| `incidentes_ultimos_7d` | Numérica | Conteo de incidentes en el sector en los últimos 7 días |
| `incidentes_ultimos_30d` | Numérica | Conteo de incidentes en el sector en los últimos 30 días |

---

## 6. PRUEBAS Y TESTEO

### 6.1 Tipos de Pruebas Aplicadas

| Tipo | Descripción | Herramienta |
|------|-------------|-------------|
| **Unitarias manuales** | Verificación de cada función de validación (PIL, rate limiting, bloqueo de cuenta) | Django shell, curl |
| **Integración** | Pruebas del flujo completo: registro → login → crear incidente → ver mapa → validar | Navegador + Railway |
| **Regresión** | Después de cada deploy, se verificó que funcionalidades previas no se rompieran | Pruebas manuales |
| **Seguridad** | Auditoría de 92+ medidas de seguridad, verificación de headers HTTP, CSP, CORS | Chrome DevTools, curl -I |
| **Compatibilidad** | Pruebas en Chrome, Firefox, Safari, móvil Android e iOS | BrowserStack / dispositivos reales |
| **Rendimiento** | Tiempos de carga de mapa, subida de imágenes, consultas a BD | Chrome DevTools Network tab |
| **Aceptación** | Pruebas con usuarios reales registrando incidentes y usando el mapa | Feedback de compañeros |

### 6.2 Plan de Pruebas

| Fase | Actividad | Criterio de aceptación |
|------|-----------|----------------------|
| **Fase 1** | Registro y login | Usuario puede registrarse, loguearse, y ver el dashboard en < 3 segundos |
| **Fase 2** | CRUD incidentes | Crear incidente con foto y GPS, listar con filtros, ver detalle completo |
| **Fase 3** | Mapa | Marcadores visibles por tipo, popups funcionales, zoom a incidente desde detalle |
| **Fase 4** | Seguridad | CSP bloquea recursos no autorizados, rate limit responde 429, login bloquea tras 5 fallos |
| **Fase 5** | Roles y permisos | Superadmin puede cambiar roles, Admin de Junta solo su sector, Vecino no ve gestión de usuarios |
| **Fase 6** | Despliegue | Railway sirve la app en HTTPS, Cloudinary sirve imágenes, WhiteNoise sirve estáticos |
| **Fase 7** | Móvil | Diseño responsivo funciona, mapa usable en pantalla táctil, formularios legibles |

### 6.3 Casos de Prueba

#### Pruebas Positivas

| ID | Caso | Pasos | Resultado esperado | Estado |
|----|------|-------|-------------------|--------|
| CP-01 | Registro exitoso | Completar formulario de registro con datos válidos | Usuario creado, redirigido a login | ✅ Pass |
| CP-02 | Login exitoso | Usuario y contraseña correctos | Sesión iniciada, redirigido a dashboard | ✅ Pass |
| CP-03 | Crear incidente con GPS | Clic en "Reportar", permitir GPS, completar formulario, subir foto, enviar | Incidente creado con coordenadas GPS y foto en Cloudinary | ✅ Pass |
| CP-04 | Mapa muestra marcadores | Ir a Mapa desde el menú | Mapa con Google Maps tiles y circleMarkers coloreados por tipo | ✅ Pass |
| CP-05 | Zoom a incidente | Desde detalle, clic en "Ver en Mapa" | Mapa centrado en coordenadas del incidente con zoom 17 | ✅ Pass |
| CP-06 | Validar incidente | Admin de Junta marca incidente como "validado" en bandeja | Incidente cambia a estado "Validado", badge verde en detalle | ✅ Pass |
| CP-07 | Cambiar rol | Superadmin clic en "Rol" en lista de usuarios, selecciona nuevo rol, guarda | Rol actualizado, AuditLog registra el cambio | ✅ Pass |
| CP-08 | Bloqueo por login fallido | Fallar login 5 veces con mismo usuario | Cuenta bloqueada, `is_active=False`, no puede loguearse | ✅ Pass |
| CP-09 | Subir imagen PNG | En crear incidente, adjuntar PNG de 2MB | Imagen validada por PIL, subida a Cloudinary, visible en detalle | ✅ Pass |

#### Pruebas Negativas

| ID | Caso | Pasos | Resultado esperado | Estado |
|----|------|-------|-------------------|--------|
| CN-01 | Login con credenciales incorrectas | Usuario no existe o contraseña mala | Mensaje de error genérico (sin revelar si usuario existe) | ✅ Pass |
| CN-02 | Rate limit login | Fallar login 10 veces desde misma IP | HTTP 429 "Demasiados intentos" con Retry-After: 900 | ✅ Pass |
| CN-03 | Subir archivo .exe como imagen | En crear incidente, seleccionar archivo .exe con extensión .jpg | PIL.verify() detecta que no es imagen, ValidationError | ✅ Pass |
| CN-04 | Subir imagen > 5MB | En crear incidente, seleccionar imagen de 8MB | ValidationError "La imagen no debe superar los 5MB" | ✅ Pass |
| CN-05 | Path traversal en /media/ | GET /media/../../etc/passwd | Http404 (os.path.normpath + startswith check) | ✅ Pass |
| CN-06 | Sin autenticación | GET /incidentes/ sin sesión | Redirigido a /login/ | ✅ Pass |
| CN-07 | Vecino intenta validar | GET /incidentes/bandeja-validacion/ como Vecino | Test func rechaza acceso, 403 | ✅ Pass |
| CN-08 | Vecino intenta cambiar rol | GET /usuarios/1/rol/ como Vecino | Test func rechaza acceso, 403 | ✅ Pass |
| CN-09 | Registro duplicado (mismo username) | Registrar "admin" cuando ya existe | Error de validación: username ya existe | ✅ Pass |
| CN-10 | 11 reportes en 1 hora | Crear 11 incidentes en <1 hora | El 11ro es rechazado con mensaje de límite alcanzado | ✅ Pass |

#### Pruebas de Límite

| ID | Caso | Pasos | Resultado esperado | Estado |
|----|------|-------|-------------------|--------|
| CL-01 | Login justo en el límite (9 intentos) | Fallar login 9 veces, luego acertar | Login exitoso al décimo intento (no es fallido) | ✅ Pass |
| CL-02 | 10 reportes en 1 hora (límite exacto) | Crear exactamente 10 incidentes en 1 hora | Los 10 se crean, el 11mo se rechaza | ✅ Pass |
| CL-03 | 3 registros en 1 hora (límite exacto) | Registrar 3 usuarios desde misma IP en 1 hora | Los 3 se crean, el 4to da 429 | ✅ Pass |
| CL-04 | Imagen justo en 5MB | Subir imagen de exactamente 5,242,880 bytes | Imagen aceptada (≤5MB) | ✅ Pass |
| CL-05 | Imagen de 1 byte más que 5MB | Subir imagen de 5,242,881 bytes | ValidationError | ✅ Pass |

### 6.4 Reporte de Pruebas

| Métrica | Valor |
|---------|-------|
| Total de casos de prueba | 24 |
| Casos pasados | 24 |
| Casos fallidos | 0 |
| Defectos encontrados y corregidos | 7 |
| Tasa de aprobación | 100% |

**Defectos corregidos durante el desarrollo:**

| ID | Defecto | Causa | Solución |
|----|---------|-------|----------|
| D-01 | Mapa no mostraba marcadores | Coma decimal española en coordenadas JS (`-17,78` en vez de `-17.78`) | `{% localize off %}` en templates |
| D-02 | Mapa completamente blanco | CDN de Leaflet bloqueado en Railway | Cambio a CDN jsDelivr + Leaflet local como respaldo |
| D-03 | Tiles OpenStreetMap devolvían 403 | IP de Railway bloqueada por OSM | Cambio a Google Maps tiles (mt1.google.com) |
| D-04 | Marcadores como cuadraditos transparentes | Imágenes de iconos Leaflet bloqueadas por CSP | Cambio a `L.circleMarker()` (sin dependencia de imágenes) |
| D-05 | Imágenes se perdían en cada redeploy | Almacenamiento efímero de Railway | Integración con Cloudinary |
| D-06 | Superadmin sin acceso a gestión de roles | `is_superuser=True` no contemplado en `test_func` | Agregar `if user.is_superuser: return True` |
| D-07 | Error 500 con `|unlocalize` | Filtro no disponible en esta versión de Django | Reemplazo por `{% localize off %}...{% endlocalize %}` |

### 6.5 Gestión de Cambios y Corrección de Errores

Se utilizó **Git** para la gestión de cambios:

- **Ramas**: `main` (producción), `backup-estable` (respaldo)
- **Tags**: `v1.0-estable` (punto de restauración)
- **Commits**: Mensajes descriptivos en español con prefijo de tipo de cambio
- **Flujo**: Cada corrección de bug se probó en desarrollo local, se commiteó, se pusheó a GitHub, y Railway desplegó automáticamente

**Convención de commits**:
```
[Fix] Corrección de bug X
[Feat] Nueva funcionalidad Y
[Security] Mejora de seguridad Z
[Style] Cambio de diseño W
[Refactor] Reestructuración de código V
```

---

## 7. CONCLUSIONES Y RECOMENDACIONES

### 7.1 Conclusiones

1. **Se logró implementar un sistema completo de reporte de incidentes** con geolocalización GPS, evidencia fotográfica, mapa interactivo y un flujo de validación comunitaria. El sistema está en producción y funcional en `https://web-production-7c95d.up.railway.app`.

2. **La seguridad informática fue una prioridad transversal**. Se implementaron más de 92 medidas de seguridad que cubren los 10 principales riesgos de OWASP: CSP, HSTS, X-Frame-Options, rate limiting, Argon2, cookies seguras, validación de archivos, path traversal protection, auditoría y manejo de errores sin fuga de información.

3. **La internacionalización al español** (`LANGUAGE_CODE='es'`, `TIME_ZONE='America/La_Paz'`) fue esencial para el público objetivo, aunque presentó desafíos técnicos con la localización de números decimales que requirieron el uso de `{% localize off %}` en las plantillas de JavaScript.

4. **El diseño responsivo y la accesibilidad** (texto grande, modo adulto mayor, tablas adaptativas en móvil) garantizan que la plataforma sea usable por ciudadanos de todas las edades y niveles de familiaridad tecnológica.

5. **La integración con Cloudinary** resolvió el problema de pérdida de archivos en deploys de Railway (disco efímero), proporcionando almacenamiento persistente para las imágenes de evidencia.

6. **La API JSON para el mapa** (`/incidentes/api/mapa/`) demostró ser más robusta que embeber datos en el template, eliminando problemas de parsing de JavaScript causados por la localización.

7. **El sistema de roles y permisos** (Vecino, Administrador de Junta Vecinal, Superadministrador) permite una gobernanza distribuida donde cada barrio puede autogestionarse.

### 7.2 Recomendaciones

1. **Implementar CAPTCHA** en los formularios de registro y login para prevenir ataques automatizados de bots.

2. **Agregar verificación de email** mediante enlace de confirmación al registrarse, mejorando la calidad de los datos de usuarios.

3. **Implementar autenticación de dos factores (2FA)** para cuentas de administradores, añadiendo una capa extra de seguridad.

4. **Desarrollar pruebas automatizadas** con `pytest-django` para prevenir regresiones en futuras iteraciones del proyecto.

5. **Expandir las predicciones de IA**: incorporar más variables (clima, eventos públicos, densidad poblacional) para mejorar la precisión del modelo.

6. **Implementar notificaciones push reales**: integrar WhatsApp Business API y Telegram Bot API para el envío de alertas.

7. **Crear una Progressive Web App (PWA)** con service worker para funcionamiento offline y notificaciones nativas en dispositivos móviles.

8. **Agregar un modo oscuro** como opción de accesibilidad adicional.

9. **Implementar internacionalización completa** (i18n) con `django-rosetta` para facilitar la traducción a otros idiomas (quechua, guaraní).

10. **Considerar migrar a PostgreSQL** si el volumen de datos crece significativamente, aprovechando PostGIS para consultas geoespaciales avanzadas.

---

## 8. REFERENCIAS BIBLIOGRÁFICAS

### Normas APA 7ª Edición

1. Django Software Foundation. (2025). *Django Documentation (Version 5.2)*. https://docs.djangoproject.com/en/5.2/

2. Cloudinary Ltd. (2024). *Cloudinary Python SDK Documentation*. https://cloudinary.com/documentation/django_integration

3. Agafonkin, V. (2023). *Leaflet.js: An Open-Source JavaScript Library for Mobile-Friendly Interactive Maps (Version 1.9.4)*. https://leafletjs.com/

4. Bootstrap Team. (2023). *Bootstrap 5.3 Documentation*. https://getbootstrap.com/docs/5.3/

5. Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... & Duchesnay, É. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research*, 12, 2825-2830. https://scikit-learn.org/

6. McKinney, W. (2010). Data Structures for Statistical Computing in Python. *Proceedings of the 9th Python in Science Conference*, 51-56. https://pandas.pydata.org/

7. Railway Corp. (2024). *Railway Documentation: Deploy Django Apps*. https://docs.railway.app/

8. Gunicorn Developers. (2024). *Gunicorn: Python WSGI HTTP Server for UNIX*. https://gunicorn.org/

9. Evans, D. (2024). *WhiteNoise: Radically simplified static file serving for Python web apps*. https://whitenoise.readthedocs.io/

10. Biryukov, A., Dinu, D., & Khovratovich, D. (2016). Argon2: New generation of memory-hard functions for password hashing and other applications. *2016 IEEE European Symposium on Security and Privacy (EuroS&P)*, 292-302. https://doi.org/10.1109/EuroSP.2016.31

11. OWASP Foundation. (2023). *OWASP Top 10 Web Application Security Risks*. https://owasp.org/www-project-top-ten/

12. Schwaber, K., & Sutherland, J. (2020). *The Scrum Guide: The Definitive Guide to Scrum: The Rules of the Game*. https://scrumguides.org/

13. Institute of Electrical and Electronics Engineers. (1998). *IEEE Std 830-1998: IEEE Recommended Practice for Software Requirements Specifications*. https://doi.org/10.1109/IEEESTD.1998.88286

14. Google LLC. (2024). *Google Maps Platform Documentation*. https://developers.google.com/maps

15. Van Rossum, G., & Drake, F. L. (2009). *Python 3 Reference Manual*. CreateSpace. https://docs.python.org/3/

---

## 9. ANEXOS

### 9.1 Capturas de Pantalla del Sistema

*(Las capturas se encuentran disponibles en producción. A continuación se describen las pantallas principales.)*

| Pantalla | Descripción |
|----------|-------------|
| Login | Formulario de inicio de sesión con diseño glassmorphism y protección rate-limiting |
| Registro | Formulario de registro público con selección de sector |
| Dashboard | Panel principal con tarjetas de acceso rápido |
| Lista de Incidentes | Tabla con filtros avanzados y paginación |
| Crear Incidente | Panel dividido: mapa interactivo con GPS + formulario de reporte |
| Detalle de Incidente | Metadata completa, coordenadas, evidencia fotográfica, testimonios |
| Mapa General | Google Maps con circleMarkers coloreados por tipo de delito |
| Validación | Bandeja de incidentes pendientes para administradores |
| Gestión de Usuarios | Lista de usuarios con indicadores de reportes falsos y botones de cambio de rol |
| Cambio de Rol | Formulario para modificar rol, estado y sector de un usuario |

### 9.2 Enlace al Repositorio GitHub

**Repositorio**: https://github.com/SrHeath/SantaCruzSegura

**Rama principal**: `main`

**Tag estable**: `v1.0-estable` (`git checkout v1.0-estable` para volver atrás)

### 9.3 Manual de Usuario

#### Registro

1. Acceder a la página de inicio
2. Hacer clic en **"Registrarse"**
3. Completar: nombre de usuario, nombre completo, email, contraseña, confirmar contraseña, sector
4. Clic en **"Crear Cuenta"**
5. Iniciar sesión con las credenciales

#### Reportar un Incidente

1. Iniciar sesión
2. Clic en **"Reportar"** en el menú de navegación
3. **Permitir acceso al GPS** cuando el navegador lo solicite
4. Si el GPS funciona: el marcador se posiciona automáticamente. Si no, arrastrar el marcador o hacer clic en el mapa
5. Completar el formulario: título, tipo de delito, sector, dirección, descripción
6. Opcional: adjuntar una imagen (JPG, PNG, WebP, máximo 5MB)
7. Clic en **"Guardar Incidente"**

#### Ver el Mapa

1. Clic en **"Mapa"** en el menú
2. Los incidentes aparecen como círculos de colores: 🔴 Robo, 🟠 Asalto, 🔵 Otro
3. Clic en un círculo para ver detalles y foto
4. Desde cualquier detalle, clic en "Ver en Mapa" para hacer zoom al incidente

#### Validar Incidentes (Administrador de Junta / Superadmin)

1. Clic en **"Validación"** en el menú
2. Revisar incidentes pendientes
3. Clic en **"Validar"** si el incidente es legítimo
4. Clic en **"Descartar"** si es falso

#### Gestionar Roles (Superadmin / Admin de Junta)

1. Clic en **"Usuarios"** en el menú
2. Buscar al usuario en la lista
3. Clic en el botón **"Rol"** en la columna Acciones
4. Seleccionar nuevo rol, estado o sector
5. Clic en **"Guardar Cambios"**

#### Suscribirse a Alertas

1. Clic en **"Suscripción"** en el menú
2. Seleccionar el sector de interés
3. Elegir canal preferido: WhatsApp, Telegram o ambos
4. Activar/desactivar alertas predictivas
5. Clic en **"Guardar"**

---

> **Documento generado el 3 de junio de 2026. Versión 1.0**
> **Proyecto: Santa Cruz Segura Predictiva**
> **Desplegado en: Railway.app**
> **Repositorio: https://github.com/SrHeath/SantaCruzSegura**
