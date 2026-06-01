import os
import pickle
import math
from datetime import datetime, timedelta
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from django.conf import settings
from django.utils import timezone

from incidentes.models import Incidente
from .models import ModeloIA

MODELS_DIR = os.path.join(settings.BASE_DIR, 'saved_models')

def retrain_model_automatic(force=False):
    """
    Función de reentrenamiento.
    - Requiere al menos 100 incidentes validados (se puede forzar para testing).
    - Divide en 80% train / 20% test.
    - Si precisión >= 70%, guarda el modelo y lo activa en la BD.
    """
    # Crear directorio si no existe
    if not os.path.exists(MODELS_DIR):
        os.makedirs(MODELS_DIR)

    # Filtrar solo incidentes validados
    registros = Incidente.objects.filter(estado='validado', activo=True)
    total_registros = registros.count()

    if total_registros < 100 and not force:
        print(f"Omitiendo reentrenamiento: Se requieren mínimo 100 registros. Actual: {total_registros}")
        return False, "Registros insuficientes (mínimo 100)"

    if total_registros < 5:  # Límite técnico mínimo para poder entrenar y dividir
        return False, "Registros insuficientes para entrenar"

    df = pd.DataFrame.from_records([
        {
            'lat': float(i.latitud),
            'lng': float(i.longitud),
            'sector': i.sector_id,
            'tipo': i.tipo_id,
            'target': 1 if i.activo else 0,
        }
        for i in registros
    ])

    X = df[['lat', 'lng', 'sector', 'tipo']]
    y = df['target']

    # División 80% entrenamiento, 20% pruebas
    if len(df) >= 10:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    else:
        # Si hay muy pocos datos, no se puede hacer split útil, usar todo para entrenar y test
        X_train, X_test, y_train, y_test = X, X, y, y

    # Entrenar RandomForest
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # Evaluar precisión
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred) * 100  # En porcentaje

    version = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(MODELS_DIR, f"model_rf_{version}.pkl")

    # Guardar temporalmente para ver si pasa el umbral del 70%
    if accuracy >= 70.0:
        # Guardar archivo
        with open(file_path, 'wb') as f:
            pickle.dump(clf, f)

        # Desactivar modelos anteriores
        ModeloIA.objects.filter(estado='activo').update(estado='inactivo')

        # Registrar en la BD
        ModeloIA.objects.create(
            version=version,
            precision_obtenida=accuracy,
            registros_usados=total_registros,
            estado='activo',
            ruta_archivo=file_path
        )
        return True, f"Modelo reentrenado con éxito. Versión {version}, precisión {accuracy:.2f}%."
    else:
        # Descartado si no cumple la precisión mínima
        ModeloIA.objects.create(
            version=version,
            precision_obtenida=accuracy,
            registros_usados=total_registros,
            estado='descartado',
            ruta_archivo=''
        )
        
        # Generar alerta para el superadmin (simulada)
        from alertas.models import Alerta
        Alerta.objects.create(
            incidente=None,
            mensaje=f"ALERTA IA: El reentrenamiento falló al no superar la precisión mínima. Precisión obtenida: {accuracy:.2f}%. Se conserva modelo anterior.",
        )
        return False, f"Descartado: Precisión de {accuracy:.2f}% es menor al 70.0% requerido."


def predecir_riesgo(lat, lng, sector_id, tipo_id):
    # Buscar el modelo IA activo en la BD
    modelo_db = ModeloIA.objects.filter(estado='activo').order_by('-fecha_entrenamiento').first()
    
    # Si no hay modelo activo, intentar reentrenar/crear uno base forzando
    if not modelo_db or not os.path.exists(modelo_db.ruta_archivo):
        exito, msg = retrain_model_automatic(force=True)
        modelo_db = ModeloIA.objects.filter(estado='activo').order_by('-fecha_entrenamiento').first()
        if not modelo_db or not os.path.exists(modelo_db.ruta_archivo):
            # Fallback en caso de no poder entrenar nada (sin datos en BD)
            # Retornar una probabilidad ficticia/aleatoria estable
            return 0.25

    try:
        with open(modelo_db.ruta_archivo, 'rb') as f:
            clf = pickle.load(f)
        
        prob = clf.predict_proba([[float(lat), float(lng), int(sector_id), int(tipo_id)]])
        return float(prob[0][1])
    except Exception as e:
        print(f"Error al predecir: {e}")
        return 0.5

