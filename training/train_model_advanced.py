import pandas as pd
import joblib
import numpy as np
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

from imblearn.over_sampling import SMOTE

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, BatchNormalization, Dropout
from tensorflow.keras.regularizers import l2
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint

# ======================
# CARREGAR BASE
# ======================

df = pd.read_csv("data/anemia_dataset_filtrado.csv")

# ======================
# FEATURES E TARGET
# ======================

X = df.drop("Diagnosis", axis=1)
y = df["Diagnosis"]

# ======================
# ENCODER
# ======================

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# ======================
# NORMALIZAÇÃO
# ======================

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ======================
# DIVISÃO
# ======================

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y_encoded,
    test_size=0.2,
    random_state=42,
    stratify=y_encoded
)

X_train_val, X_val, y_train_val, y_val = train_test_split(
    X_train,
    y_train,
    test_size=0.2,
    random_state=42,
    stratify=y_train
)

# ======================
# APLICAR SMOTE
# ======================

print("\n" + "="*70)
print("APLICANDO SMOTE NO CONJUNTO DE TREINAMENTO")
print("="*70)

sm = SMOTE(random_state=42, k_neighbors=1)
X_train_res, y_train_res = sm.fit_resample(X_train_val, y_train_val)

print(f"Após SMOTE:")
print(f"  Amostras de treino: {len(X_train_res)}")
print(f"  Distribuição das classes: {np.bincount(y_train_res)}")

# ======================
# 1. KNN COM DIFERENTES K
# ======================

print("\n" + "="*70)
print("TESTANDO KNN COM DIFERENTES K")
print("="*70 + "\n")

knn_results = {}
best_knn = None
best_knn_k = None
best_knn_accuracy = 0

for k in [3, 5, 7, 9, 11, 15]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_res, y_train_res)

    accuracy = accuracy_score(y_test, knn.predict(X_test))
    cv_scores = cross_val_score(knn, X_scaled, y_encoded, cv=5)

    knn_results[k] = accuracy
    print(f"KNN (K={k:2d}): {accuracy:.4f} | CV: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")

    if accuracy > best_knn_accuracy:
        best_knn_accuracy = accuracy
        best_knn = knn
        best_knn_k = k

print(f"\n✓ Melhor KNN: K={best_knn_k} com acurácia {best_knn_accuracy:.4f}")

# ======================
# 2. SVM COM GRID SEARCH
# ======================

print("\n" + "="*70)
print("TESTANDO SVM COM GRID SEARCH")
print("="*70 + "\n")

svm_params = {
    'kernel': ['linear', 'rbf', 'poly'],
    'C': [0.1, 1, 10, 16, 100],
    'gamma': ['scale', 'auto']
}

svm = SVC(probability=True, random_state=42)
grid_search = GridSearchCV(svm, svm_params, cv=5, n_jobs=-1, verbose=1)
grid_search.fit(X_train_res, y_train_res)

best_svm = grid_search.best_estimator_
best_svm_accuracy = accuracy_score(y_test, best_svm.predict(X_test))
best_svm_params = grid_search.best_params_

print(f"\n✓ Melhor SVM: {best_svm_params}")
print(f"  Acurácia: {best_svm_accuracy:.4f}")

# ======================
# 3. REDE NEURAL
# ======================

print("\n" + "="*70)
print("TREINANDO REDE NEURAL")
print("="*70 + "\n")

def create_neural_network(X):
    model = Sequential([
        Dense(512, activation='relu', input_shape=(X.shape[1],), kernel_regularizer=l2(0.001)),
        BatchNormalization(),
        Dropout(0.3),

        Dense(256, activation='relu', kernel_regularizer=l2(0.001)),
        BatchNormalization(),
        Dropout(0.3),

        Dense(128, activation='relu'),
        Dropout(0.2),

        Dense(9, activation='softmax')
    ])
    return model

model_nn = create_neural_network(X_train_res)

adam = tf.keras.optimizers.Adam(learning_rate=0.001)

model_nn.compile(
    loss='sparse_categorical_crossentropy',
    optimizer=adam,
    metrics=['accuracy']
)

callbacks = [
    EarlyStopping(monitor='val_loss', patience=15, restore_best_weights=True),
    ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=7, min_lr=1e-6),
    ModelCheckpoint('models/best_neural_model.keras', monitor='val_accuracy', save_best_only=True)
]

history = model_nn.fit(
    X_train_res,
    y_train_res,
    epochs=200,
    batch_size=32,
    validation_data=(X_val, y_val),
    shuffle=True,
    callbacks=callbacks,
    verbose=1
)

# Avaliar no teste
y_pred_nn = model_nn.predict(X_test, verbose=0)
y_pred_nn_classes = np.argmax(y_pred_nn, axis=1)
best_nn_accuracy = accuracy_score(y_test, y_pred_nn_classes)

print(f"\n✓ Rede Neural: Acurácia {best_nn_accuracy:.4f}")

# ======================
# COMPARAÇÃO FINAL
# ======================

print("\n" + "="*70)
print("COMPARACAO FINAL DOS MODELOS")
print("="*70)

models_final = {
    f"KNN (K={best_knn_k})": (best_knn, best_knn_accuracy),
    f"SVM {best_svm_params}": (best_svm, best_svm_accuracy),
    "Rede Neural": (model_nn, best_nn_accuracy)
}

for name, (model, accuracy) in models_final.items():
    print(f"{name}: {accuracy:.4f}")

# Escolher melhor modelo
best_model_name = max(models_final.items(), key=lambda x: x[1][1])[0]
best_model = models_final[best_model_name][0]
best_accuracy = models_final[best_model_name][1]

print(f"\n" + "="*70)
print(f"MELHOR MODELO: {best_model_name}")
print(f"Acurácia: {best_accuracy:.4f}")
print("="*70)

# ======================
# SALVAR MODELOS
# ======================

# Salvar o melhor modelo
if best_model_name.startswith("Rede Neural"):
    model_nn.save("models/best_model.keras")
    print(f"\nModelo Rede Neural salvo como 'best_model.keras'")
else:
    joblib.dump(best_model, "models/decision_tree_model.pkl")
    print(f"\nModelo {best_model_name} salvo como 'decision_tree_model.pkl'")

# Salvar sempre o scaler e label encoder
joblib.dump(scaler, "models/scaler.pkl")
joblib.dump(label_encoder, "models/label_encoder.pkl")

print("Scaler e Label Encoder salvos com sucesso!")

# ======================
# RELATORIO DETALHADO
# ======================

print("\n" + "="*70)
print("RELATORIO DETALHADO DO MELHOR MODELO")
print("="*70 + "\n")

if best_model_name.startswith("Rede Neural"):
    y_pred = np.argmax(model_nn.predict(X_test, verbose=0), axis=1)
else:
    y_pred = best_model.predict(X_test)

print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))
