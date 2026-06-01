# 🛡️ Santa Cruz Segura Predictiva

**Sistema integral de reportes de incidentes y predicción de zonas de riesgo**

## 📋 Descripción

Santa Cruz Segura Predictiva es una aplicación web completa desarrollada con Django y MySQL que permite:

✅ **Gestión de usuarios** - Registro, login y roles (Superadministrador, Admin, Policía, Vecino)
✅ **Reportes de incidentes** - Crear reportes con geolocalización e imágenes
✅ **Mapas interactivos** - Visualización con heatmap de zonas de riesgo
✅ **Predicciones ML** - Cálculo de probabilidad de riesgo en zonas específicas
✅ **Estadísticas** - Dashboard con gráficos y reportes en PDF
✅ **Auditoría** - Registro de todas las acciones de usuarios
✅ **Alertas** - Sistema de alertas para incidentes críticos

---

## 🎯 Características principales

### 🔐 **Autenticación y autorización**
- Sistema de login seguro
- Registro de nuevos usuarios
- Roles y permisos granulares
- Dashboard personalizado por rol

### 📍 **Reportes de incidentes**
- Crear reportes con coordenadas GPS
- Clasificación por sector y tipo de delito
- Subida de imágenes
- Historial de modificaciones

### 🗺️ **Visualización de datos**
- Mapa interactivo con Leaflet
- Heatmap de densidad de incidentes
- Marcadores coloreados por tipo
- Información al hacer clic

### 🤖 **Machine Learning**
- RandomForest para predicción de riesgo
- Entrenamiento automático con datos históricos
- Cálculo de probabilidad en tiempo real
- Historial de predicciones

### 📊 **Reportes**
- Estadísticas por tipo y sector
- Gráficos interactivos
- **Exportación a PDF**

### 📝 **Auditoría**
- Registro de creación/modificación de incidentes
- Usuario responsable
- Timestamp automático

---

## 🚀 Inicio rápido

### Requisitos
- Python 3.11+
- MySQL 8.x
- pip

### Instalación

1. **Clonar o descargar el proyecto**
```bash
cd santa_cruz_segura
```

2. **Crear virtual environment**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

3. **Instalar dependencias**
```powershell
pip install -r requirements.txt
```

4. **Crear base de datos MySQL**
```sql
CREATE DATABASE santa_cruz_segura CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'santacruz'@'localhost' IDENTIFIED BY 'TuPasswordSeguro';
GRANT ALL PRIVILEGES ON santa_cruz_segura.* TO 'santacruz'@'localhost';
FLUSH PRIVILEGES;
```

5. **Configurar y migrar**
```powershell
python manage.py makemigrations
python manage.py migrate
```

6. **Crear superusuario**
```powershell
python manage.py createsuperuser
```

7. **Crear datos iniciales**
```powershell
python manage.py crear_datos
```

8. **Ejecutar servidor**
```powershell
python manage.py runserver
```

Accede a: **http://127.0.0.1:8000**

---

## 📁 Estructura del proyecto

```
santa_cruz_segura/
├── usuarios/              # Autenticación y gestión de usuarios
├── incidentes/            # Reportes de incidentes
├── auditoria/             # Registro de auditoría
├── alertas/               # Sistema de alertas
├── estadisticas/          # Dashboard y reportes
├── predicciones/          # ML y predicciones
├── templates/             # Templates HTML
│   └── base.html, login.html, dashboard.html, etc.
├── static/                # CSS, JS, imágenes
├── media/                 # Fotos y audios subidos
├── requirements.txt       # Dependencias Python
├── manage.py              # CLI de Django
└── INSTALACION.md         # Guía completa de instalación
```

---

## 🎮 Flujo de usuario

### **1. Registro**
- Accede a `/registro/`
- Completa formulario con datos personales
- Selecciona tu rol
- Contraseña segura

### **2. Login**
- Ingresa a `/login/`
- Usuario y contraseña
- Redireccionamiento al dashboard

### **3. Dashboard**
- Panel de bienvenida con accesos rápidos
- Menú principal con todas las opciones

### **4. Reportar incidente**
- Navega a "Reportar"
- Completa formulario:
  - Título y descripción
  - Ubicación (latitud/longitud)
  - Sector y tipo de delito
  - Foto (opcional)
- Se guarda automáticamente

### **5. Visualización**
- **Mapa**: Ver todos los incidentes con heatmap
- **Estadísticas**: Gráficos por tipo y sector
- **Predicciones**: Calcular riesgo en una zona

### **6. Alertas**
- Se generan automáticamente
- Lista de alertas recientes

---

## 👥 Roles y permisos

| Permiso | Super | Admin | Policía | Vecino |
|---------|-------|-------|---------|--------|
| Crear usuarios | ✅ | ❌ | ❌ | ❌ |
| Ver usuarios | ✅ | ✅ | ❌ | ❌ |
| Crear incidentes | ✅ | ✅ | ✅ | ✅ |
| Ver incidentes | ✅ | ✅ | ✅ | ✅ |
| Ver reportes PDF | ✅ | ✅ | ✅ | ❌ |
| Ver predicciones | ✅ | ✅ | ✅ | ❌ |
| Panel admin | ✅ | ❌ | ❌ | ❌ |

---

## 🛠️ Tecnologías usadas

- **Backend**: Django 5.2, Python 3.11
- **Base de datos**: MySQL 8.x
- **Frontend**: Bootstrap 5.3, Leaflet.js
- **ML**: scikit-learn, pandas
- **Reportes**: reportlab
- **Mapas**: OpenStreetMap, Leaflet.heat

---

## 📚 APIs disponibles

### **Mapa de calor (GeoJSON)**
```
GET /predicciones/api/mapa-calor/
```
Retorna todos los incidentes activos en formato GeoJSON

---

## 🐛 Troubleshooting

### ❌ Error: "No module named 'mysqlclient'"
```powershell
pip install mysqlclient
# En Windows, si falla:
pip install pymysql
```

### ❌ Error: "Connection refused"
- Verifica que MySQL esté corriendo
- Comprueba credenciales en `settings.py`

### ❌ Error: "Tabla no existe"
```powershell
python manage.py migrate
```

---

## 📖 Documentación completa

Ver [INSTALACION.md](INSTALACION.md) para:
- Guía paso a paso completa
- Solución de problemas detallada
- Configuración avanzada
- Management commands

---

## ✅ Checklist de verificación

```
☐ Python 3.11+ instalado
☐ MySQL corriendo en localhost:3306
☐ Virtual environment activado
☐ Requirements instalados
☐ Migraciones aplicadas
☐ Superusuario creado
☐ Datos iniciales creados (python manage.py crear_datos)
☐ Servidor corriendo en http://127.0.0.1:8000
☐ Login funciona
☐ Puedes crear incidentes
☐ Mapa muestra heatmap
☐ PDF se descarga correctamente
```

---

## 🔮 Próximas mejoras

- 📱 App móvil con React Native
- 🔔 Notificaciones por email
- 🗺️ Integración con Google Maps
- 🤖 Modelos ML más avanzados
- 📈 Dashboard con D3.js
- 🎫 Sistema de tickets
- 🌐 Integración con redes sociales

---

## 📞 Contacto y soporte

Para bugs, sugerencias o preguntas: contacta al equipo de desarrollo

**Versión**: 1.0  
**Última actualización**: Enero 2025  
**Licencia**: Código de fuente abierta

---

## 📝 Licencia

Este proyecto está bajo licencia de código abierto. Úsalo libremente en tus proyectos.

---

**¡Gracias por usar Santa Cruz Segura Predictiva! 🛡️**
