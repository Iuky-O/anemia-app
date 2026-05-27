import streamlit as st
import pandas as pd
import joblib

from utils.anemia_descriptions import ANEMIA_INFO

# ======================
# CARREGAR MODELOS
# ======================

model = joblib.load("models/svm_model_91.pkl")
scaler = joblib.load("models/scaler.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")

st.title("🧠 Predição de Anemia")

st.write("Preencha os parâmetros abaixo:")

# ======================
# INPUTS
# ======================

HGB = st.number_input("HGB")
PLT = st.number_input("PLT")
WBC = st.number_input("WBC")
RBC = st.number_input("RBC")
MCV = st.number_input("MCV")
MCH = st.number_input("MCH")
MCHC = st.number_input("MCHC")

# ======================
# BOTÃO
# ======================

if st.button("Classificar"):

    data = pd.DataFrame([[
        HGB,
        PLT,
        WBC,
        RBC,
        MCV,
        MCH,
        MCHC
    ]], columns=[
        "HGB",
        "PLT",
        "WBC",
        "RBC",
        "MCV",
        "MCH",
        "MCHC"
    ])

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
