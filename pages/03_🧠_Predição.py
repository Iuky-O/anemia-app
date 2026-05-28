import streamlit as st
import pandas as pd
import joblib

from utils.anemia_descriptions import ANEMIA_INFO

# ======================
# CARREGAR MODELOS
# ======================

model = joblib.load("models/svm_model.pkl")
scaler = joblib.load("models/scaler.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")

df_reference = pd.read_csv("data/anemia_dataset_filtrado.csv")
feature_columns = df_reference.drop("Diagnosis", axis=1).columns.tolist()

st.title("🧠 Predição de Anemia")

st.write("Preencha os parâmetros abaixo:")

# ======================
# INPUTS
# ======================

HGB = st.number_input("HGB")
RBC = st.number_input("RBC")
MCV = st.number_input("MCV")
MCH = st.number_input("MCH")
MCHC = st.number_input("MCHC")
PLT = st.number_input("PLT")
WBC = st.number_input("WBC")

# ======================
# BOTÃO
# ======================

if st.button("Classificar"):

    def normalize_number(value):
        if isinstance(value, str):
            value = value.replace(",", ".")
        return float(value)

    data = pd.DataFrame([[
        normalize_number(HGB),
        normalize_number(RBC),
        normalize_number(MCV),
        normalize_number(MCH),
        normalize_number(MCHC),
        normalize_number(PLT),
        normalize_number(WBC)
    ]], columns=feature_columns)

    data_scaled = scaler.transform(data)

    prediction = model.predict(data_scaled)

    probabilities = model.predict_proba(data_scaled)

    result = label_encoder.inverse_transform(prediction)

    prediction_name = result[0]

    st.success(f"Diagnóstico: {prediction_name}")

    # ======================
    # PROBABILIDADES
    # ======================

    st.subheader("Probabilidades")

    for i, class_name in enumerate(label_encoder.classes_):
        st.write(
            f"{class_name}: {probabilities[0][i] * 100:.2f}%"
        )

    # ======================
    # EXPLICAÇÃO DA DOENÇA
    # ======================

    if prediction_name in ANEMIA_INFO:

        info = ANEMIA_INFO[prediction_name]

        st.divider()

        with st.expander("📚 Ver detalhes sobre o diagnóstico"):

            st.header(info['title'])

            st.write(info["description"])

            st.subheader("Possíveis sintomas")

            for symptom in info["symptoms"]:
                st.write(f"- {symptom}")

            st.subheader("Características laboratoriais")

            for characteristic in info["characteristics"]:
                st.write(f"- {characteristic}")
