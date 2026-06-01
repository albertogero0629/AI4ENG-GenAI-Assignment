import pandas as pd

def alinear_eventos_con_referencias(
    eventos: pd.DataFrame,
    referencias: pd.DataFrame,
    columna_tiempo: str,
    columna_valor: str
) -> pd.DataFrame:
    """
    Alinea eventos con el valor de referencia más reciente disponible en el tiempo.
    """
    # 5. No modificar los DataFrames originales
    df_ev = eventos.copy()
    df_ref = referencias.copy()
    
    # 1. Ordenar ambos DataFrames por la columna columna_tiempo
    df_ev = df_ev.sort_values(by=columna_tiempo)
    df_ref = df_ref.sort_values(by=columna_tiempo)
    
    # Preparamos el DataFrame de referencias aislando solo las columnas útiles 
    # y renombrando la columna de valor para cumplir con el requisito 3.
    df_ref = df_ref[[columna_tiempo, columna_valor]].rename(
        columns={columna_valor: 'valor_referencia'}
    )
    
    # 2. Realizar unión utilizando pd.merge_asof sin utilizar valores futuros
    # direction='backward' (que es el valor por defecto) garantiza que busque
    # el valor más reciente hacia atrás en el tiempo.
    resultado = pd.merge_asof(
        df_ev,
        df_ref,
        on=columna_tiempo,
        direction='backward'
    )
    
    # 6. Devolver el DataFrame resultante
    return resultado
