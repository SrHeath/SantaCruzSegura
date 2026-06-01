# Guía de Instalación del Proyecto en Windows desde Cero

Esta guía está diseñada para que cualquier desarrollador o colega pueda instalar y ejecutar el proyecto **Santa Cruz Segura Predictiva** en una computadora con sistema operativo Windows, partiendo desde cero (sin herramientas previamente instaladas).

---

## 📋 Requisitos de la Guía
A continuación se describen detalladamente los pasos para instalar las herramientas necesarias, configurar la base de datos, entrenar la IA e iniciar la aplicación.

---

## 🛠️ Paso 1: Instalar Python en Windows
Si tu no tiene Python instalado, debe seguir estos pasos obligatorios:

1. **Descargar Python**:
   * Ir a la página oficial de descargas: [python.org/downloads](https://www.python.org/downloads/)
   * Descargar la versión recomendada de Python para Windows (versión **3.11.x** o **3.12.x**).
2. **Ejecutar el Instalador**:
   * Hacer doble clic en el archivo `.exe` descargado.
   * **⚠️ IMPORTANTE (CRÍTICO)**: Antes de presionar cualquier botón de instalar, se debe marcar la casilla en la parte inferior que dice **"Add python.exe to PATH"** (Agregar python.exe al PATH). Si no se activa esto, la consola de Windows no reconocerá los comandos `python` ni `pip`.
   * Hacer clic en **"Install Now"** (Instalar Ahora).
3. **Verificar la Instalación**:
   * Abrir una consola (PowerShell o CMD) y ejecutar:
     ```powershell
     python --version
     pip --version
     ```
   * Ambos comandos deben retornar la versión instalada.

---

## 💾 Paso 2: Instalar y Configurar MySQL Server
El proyecto utiliza MySQL como motor de base de datos relacional.

1. **Descargar MySQL**:
   * Descargar el instalador de MySQL para Windows: [dev.mysql.com/downloads/installer/](https://dev.mysql.com/downloads/installer/)
   * Seleccionar la opción de descarga más completa e iniciar la instalación.
2. **Instalación Recomendada**:
   * Seleccionar el tipo de instalación **"Developer Default"** o simplemente instalar **MySQL Server** y **MySQL Workbench** (interfaz gráfica).
   * Durante la configuración de seguridad, ingresar una contraseña para el usuario administrador `root` y recordarla.
3. **Crear la Base de Datos**:
   * Abrir **MySQL Workbench** o la línea de comandos de MySQL.
   * Ejecutar la creación de la base de datos y el usuario exclusivo del proyecto:
     ```sql
     -- 1. Crear Base de Datos
     CREATE DATABASE santa_cruz_segura CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

     -- 2. Crear Usuario para el Proyecto
     CREATE USER 'santacruz'@'localhost' IDENTIFIED BY 'TuPasswordSeguro';

     -- 3. Conceder Permisos
     GRANT ALL PRIVILEGES ON santa_cruz_segura.* TO 'santacruz'@'localhost';
     FLUSH PRIVILEGES;
     ```

> [!NOTE]
> Las credenciales de acceso de la base de datos están especificadas en el archivo `santa_cruz_segura/settings.py`. Si decides usar el usuario `root` u otra contraseña, debes cambiar esos valores en dicho archivo.

---

## 📂 Paso 3: Descargar y Abrir el Proyecto
1. Descargar o extraer los archivos del código en una carpeta local (por ejemplo: `C:\Proyectos\santa_cruz_segura`).
2. Abrir la consola (PowerShell o CMD) y navegar a la carpeta raíz del proyecto:
   ```powershell
   cd "D:\Desarrolo de Sistemas 2\santa_cruz_segura"  # Reemplazar por la ruta donde esté guardado
   ```

---

## 🐍 Paso 4: Crear y Activar el Entorno Virtual (Venv)
El entorno virtual sirve para instalar las librerías del proyecto sin alterar el sistema de forma global.

1. **Crear el Entorno Virtual**:
   En la consola raíz del proyecto ejecuta:
   ```powershell
   python -m venv .venv
   ```
2. **Activar el Entorno**:
   * **Si usas PowerShell**:
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
     *(Si aparece un error de restricciones de políticas de ejecución de Windows, ejecuta `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` y vuelve a intentar).*
   * **Si usas CMD (Símbolo del Sistema)**:
     ```cmd
     .\.venv\Scripts\activate.bat
     ```
   * Sabrás que está activo porque aparecerá `(.venv)` al inicio de la línea de comandos.

---

## 📦 Paso 5: Instalar las Dependencias de Python
Con el entorno virtual activado (`.venv`), ejecuta el instalador de paquetes:

```powershell
pip install -r requirements.txt
```

### 🛠️ Solución de Problemas con `mysqlclient` en Windows:
En algunas computadoras con Windows, instalar `mysqlclient` suele fallar porque exige tener instalado Microsoft Visual C++ Build Tools.
* **Solución**: El proyecto ya viene configurado para usar **PyMySQL** (una librería puramente escrita en Python que no requiere compilación C++). Si la instalación falla en `mysqlclient`:
  1. Abre el archivo `requirements.txt`.
  2. Elimina o comenta la línea que contiene `mysqlclient>=2.1`.
  3. Ejecuta de nuevo `pip install -r requirements.txt`. Todo funcionará a la perfección utilizando `pymysql` automáticamente.

---

## 🏗️ Paso 6: Configurar Estructura y Sembrar Datos
Una vez instaladas las dependencias, inicializa la estructura de datos:

1. **Crear Tablas (Migraciones)**:
   ```powershell
   python manage.py migrate
   ```
2. **Sembrar Datos de Prueba y Cuentas Iniciales**:
   ```powershell
   python manage.py crear_datos
   ```
   *Este comando semilla cargará de forma automática los tipos de delitos, los sectores y barrios con sus coordenadas geográficas reales, y creará un administrador por defecto:*
   * **Usuario**: `admin`
   * **Contraseña**: `1234`

---

## 🧠 Paso 7: Entrenar el Modelo de Inteligencia Artificial (IA)
Para que el mapa de calor de riesgo y el simulador de IA predictiva funcionen correctamente, es necesario entrenar el modelo con los incidentes base cargados en el paso anterior. Ejecuta:

```powershell
python manage.py reentrenar_ia --force
```

Este comando generará el archivo del modelo `prediccion_delito_model.pkl` de manera local.

---

## 🚀 Paso 8: Iniciar el Servidor de Desarrollo
Finalmente, arranca la aplicación ejecutando:

```powershell
python manage.py runserver
```

* **Acceso**: Abre tu navegador e ingresa a [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
* **Ingreso**: Puedes usar la cuenta `admin` con contraseña `1234` para entrar.

---

## 🔍 Solución de Errores Comunes

### 1. `python` o `pip` no se reconoce como un comando interno o externo
* **Por qué ocurre**: No marcaste la casilla "Add python.exe to PATH" durante la instalación.
* **Solución**: Vuelve a abrir el instalador de Python, selecciona "Modify" (Modificar), marca la casilla del PATH y finaliza. O agrega la ruta de instalación de Python manualmente a tus variables de entorno del sistema.

### 2. Error `django.db.utils.OperationalError: (2003, "Can't connect to MySQL server")`
* **Por qué ocurre**: El servidor de MySQL no está corriendo o el puerto/host es incorrecto.
* **Solución**: Verifica que el servicio de MySQL Server esté iniciado en Windows (puedes buscar "Servicios" en el menú de inicio de Windows y asegurarte de que `MySQL80` esté en estado "En ejecución").

### 3. Error `Port 8000 is already in use` (El puerto 8000 ya está en uso)
* **Por qué ocurre**: Hay otra instancia de Django o aplicación corriendo en ese puerto.
* **Solución**: Puedes arrancar Django en otro puerto libre ejecutando:
  ```powershell
  python manage.py runserver 8080
  ```
  E ingresas a la aplicación usando [http://127.0.0.1:8080/](http://127.0.0.1:8080/).
