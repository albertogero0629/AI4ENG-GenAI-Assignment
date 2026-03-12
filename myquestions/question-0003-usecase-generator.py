import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.svm import OneClassSVM

def generar_caso_de_uso_detectar_piezas_defectuosas():
    np.random.seed(42)
    # X_train (simula datos normales)
    X_train = np.random.normal(loc=10, scale=1, size=(50, 3))
    # X_test (simula normales y anómalos mezclados)
    X_test_normal = np.random.normal(loc=10, scale=1, size=(10, 3))
    X_test_anomalo = np.random.normal(loc=20, scale=5, size=(5, 3))
    X_test = np.vstack([X_test_normal, X_test_anomalo])
    
    # Solución esperada internamente
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    model = OneClassSVM(nu=0.1, kernel='rbf', gamma='scale')
    model.fit(X_train_scaled)
    preds = model.predict(X_test_scaled)
    
    return {
        "input": {"X_train": X_train, "X_test": X_test},
        "output": preds
    }
