import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score

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
    random_state=42
)

# ======================
# MODELOS
# ======================

models = {
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "SVM": SVC(probability=True),
    "DecisionTree": DecisionTreeClassifier(max_depth=5)
}

best_model = None
best_accuracy = 0

print("\n===== RESULTADOS =====\n")

for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"{name}: {accuracy:.4f}")

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model

# ======================
# SALVAR MODELO
# ======================

joblib.dump(best_model, "models/svm_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")
joblib.dump(label_encoder, "models/label_encoder.pkl")

print("\nMelhor modelo salvo!")