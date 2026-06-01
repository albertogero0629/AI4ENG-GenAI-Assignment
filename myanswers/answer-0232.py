import pandas as pd

def analizar_eficiencia_rutas(df, umbral_consumo):
    """
    Identifica y calcula el exceso de costo de rutas ineficientes 
    basándose en el consumo de combustible.
    """
    # Trabajamos sobre una copia para no alterar el DataFrame original
    df_rutas = df.copy()
    
    # 1. Calcular la nueva columna consumo_por_km
    df_rutas['consumo_por_km'] = df_rutas['litros_consumidos'] / df_rutas['distancia_km']
    
    # 2. Filtrar las rutas donde consumo_por_km sea superior al umbral
    df_ineficientes = df_rutas[df_rutas['consumo_por_km'] > umbral_consumo].copy()
    
    # 3. Calcular el exceso de costo (precio fijado en 5.0 por litro)
    df_ineficientes['exceso'] = (df_ineficientes['consumo_por_km'] - umbral_consumo) * df_ineficientes['distancia_km'] * 5.0
    
    # 4. Ordenar por 'exceso' de forma descendente y reiniciar el índice
    resultado = df_ineficientes.sort_values(by='exceso', ascending=False).reset_index(drop=True)
    
    return resultado
