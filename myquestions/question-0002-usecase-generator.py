import pandas as pd
import numpy as np

def generar_caso_de_uso_calcular_rotacion_inventario():
    df = pd.DataFrame({
        'product_id': [f'P{i}' for i in range(1, 6)],
        'initial_stock': [100, 50, 0, 200, 10],
        'units_sold': [80, 50, 0, 150, 5],
        'restock_units': [20, 0, 0, 50, 5]
    })
    
    # Solución esperada internamente
    res = df.copy()
    res['final_stock'] = res['initial_stock'] - res['units_sold'] + res['restock_units']
    avg_stock = (res['initial_stock'] + res['final_stock']) / 2
    res['turnover_rate'] = np.where(avg_stock == 0, 0, res['units_sold'] / avg_stock)
    res = res.sort_values('turnover_rate', ascending=False).reset_index(drop=True)
    
    return {
        "input": {"df": df},
        "output": res
    }
