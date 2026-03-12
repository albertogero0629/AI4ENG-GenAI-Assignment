import pandas as pd
import numpy as np

def generar_caso_de_uso_analizar_eficiencia_rutas():
    np.random.seed(42)
    df = pd.DataFrame({
        'route_id': np.random.choice(['R1', 'R2', 'R3', 'R4'], 20),
        'driver_id': np.random.randint(100, 105, 20),
        'planned_duration': np.random.uniform(30, 60, 20),
        'actual_duration': np.random.uniform(25, 80, 20),
        'status': np.random.choice(['completed', 'failed'], 20, p=[0.8, 0.2])
    })
    
    # Solución esperada internamente
    df_valid = df[df['status'] != 'failed'].copy()
    df_valid['delay'] = df_valid['actual_duration'] - df_valid['planned_duration']
    res = df_valid.groupby('route_id').agg(
        delay_promedio=('delay', 'mean'),
        entregas=('route_id', 'count')
    ).reset_index()
    res = res[res['entregas'] >= 3].sort_values('delay_promedio', ascending=False).reset_index(drop=True)
    
    return {
        "input": {"df": df},
        "output": res
    }
