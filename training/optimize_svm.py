import pandas as pd
import joblib
import numpy as np
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

from imblearn.over_sampling import SMOTE

# ======================
# CARREGAR E PREPARAR DADOS
# ======================

df = pd.read_csv("data/anemia_dataset_filtrado.csv")
X = df.drop("Diagnosis", axis=1)
y = df["Diagnosis"]

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
)

X_train_val, X_val, y_train_val, y_val = train_test_split(
    X_train, y_train, test_size=0.2, random_state=42, stratify=y_train
)

# Aplicar SMOTE
sm = SMOTE(random_state=42, k_neighbors=1)
X_train_res, y_train_res = sm.fit_resample(X_train_val, y_train_val)

print("\n" + "="*80)
print("GRID SEARCH EXTENSO PARA OTIMIZAR SVM")
print("="*80 + "\n")

# Grid Search mais abrangente
param_grid = {
    'kernel': ['linear', 'rbf', 'poly', 'sigmoid'],
    'C': [0.01, 0.1, 1, 10, 50, 100, 500, 1000],
    'gamma': ['scale', 'auto', 0.0001, 0.0005, 0.001, 0.01, 0.1, 1],
    'class_weight': [None, 'balanced'],
    'degree': [2, 3, 4]  # apenas para kernel='poly'
}

# SVM com Grid Search detalhado
svm = SVC(probability=True, random_state=42)

# Executar Grid Search
print("Executando Grid Search... (pode levar alguns minutos)\n")

grid_search = GridSearchCV(
    svm,
    param_grid,
    cv=5,
    n_jobs=-1,
    verbose=2,
    scoring='accuracy'
)

grid_search.fit(X_train_res, y_train_res)

# ======================
# RESULTADOS
# ======================

print("\n" + "="*80)
print("TOP 10 MELHORES COMBINACOES DE PARAMETROS")
print("="*80 + "\n")

results_df = pd.DataFrame(grid_search.cv_results_)
results_df = results_df.sort_values('rank_test_score')

for i, row in results_df.head(10).iterrows():
    params = {key: row[f'param_{key}'] for key in param_grid.keys() if f'param_{key}' in row.index}
    # Remover None values
    params = {k: v for k, v in params.items() if pd.notna(v)}

    cv_score = row['mean_test_score']
    print(f"Rank {int(row['rank_test_score'])}: CV Score = {cv_score:.4f}")
    print(f"  Parametros: {params}\n")

# ======================
# MELHOR MODELO
# ======================

best_svm = grid_search.best_estimator_
best_params = grid_search.best_params_
best_cv_score = grid_search.best_score_

print("="*80)
print("MELHOR MODELO ENCONTRADO")
print("="*80)
print(f"\nParametros: {best_params}")
print(f"CV Score: {best_cv_score:.4f}")

# Testar no conjunto de teste
y_pred = best_svm.predict(X_test)
test_accuracy = accuracy_score(y_test, y_pred)

print(f"Acurácia no Teste: {test_accuracy:.4f}")

# ======================
# RELATORIO DETALHADO
# ======================

print("\n" + "="*80)
print("RELATORIO DETALHADO")
print("="*80 + "\n")

print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

# ======================
# SALVAR MODELO
# ======================

print("="*80)
print("SALVANDO MODELO")
print("="*80)

joblib.dump(best_svm, "models/decision_tree_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")
joblib.dump(label_encoder, "models/label_encoder.pkl")

print(f"\nModelo SVM otimizado salvo!")
print(f"Acurácia Final: {test_accuracy:.4f}")

# ======================
# COMPARACAO COM MODELO ANTERIOR
# ======================

print("\n" + "="*80)
print("COMPARACAO")
print("="*80)
print(f"\nModelo Anterior (SVM kernel=rbf, C=100, gamma=auto): 88.72%")
print(f"Modelo Otimizado: {test_accuracy*100:.2f}%")
print(f"Melhoria: {(test_accuracy - 0.8872)*100:+.2f}%")
