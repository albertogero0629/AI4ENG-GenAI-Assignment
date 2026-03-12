import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.datasets import make_classification

def generar_caso_de_uso_optimizar_bosque_aleatorio():
    # Generar datos simulados de clasificación
    X, y = make_classification(n_samples=100, n_features=4, random_state=42)
    
    # Solución esperada internamente
    rf = RandomForestClassifier(random_state=42)
    param_dist = {'n_estimators': [50, 100, 200], 'max_depth': [None, 10, 20]}
    search = RandomizedSearchCV(rf, param_distributions=param_dist, n_iter=3, cv=3, random_state=42)
    search.fit(X, y)
    
    return {
        "input": {"X": X, "y": y},
        "output": {"mejores_parametros": search.best_params_}
    }
