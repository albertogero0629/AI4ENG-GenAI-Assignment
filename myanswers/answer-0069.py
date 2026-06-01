import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

def detectar_anomalias(df, contaminacion=0.05):
    """
    Detecta anomalías en un DataFrame utilizando IsolationForest.
    
    Args:
        df (pd.DataFrame): DataFrame con variables numéricas.
        contaminacion (float): Proporción de anomalías esperadas.
        
    Returns:
        np.ndarray: Array donde -1 indica anomalía y 1 indica dato normal.
    """
    # Instanciar el modelo usando la contaminación y la semilla oculta del generador
    modelo = IsolationForest(contamination=contaminacion, random_state=42)
    
    # Entrenar el modelo con los datos
    modelo.fit(df)
    
    # Predecir las anomalías sobre el mismo dataset
    predicciones = modelo.predict(df)
    
    return predicciones
