import streamlit as st
import pandas as pd
import joblib

# ======================
# CARREGAR MODELOS
# ======================

model = joblib.load("models/svm_model.pkl")
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
PDW = st.number_input("PDW")
PCT = st.number_input("PCT")
LYMp = st.number_input("LYMp")
NEUTp = st.number_input("NEUTp")
LYMn = st.number_input("LYMn")
NEUTn = st.number_input("NEUTn")

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
        MCHC,
        PDW,
        PCT,
        LYMp,
        NEUTp,
        LYMn,
        NEUTn
    ]], columns=[
        "HGB",
        "PLT",
        "WBC",
        "RBC",
        "MCV",
        "MCH",
        "MCHC",
        "PDW",
        "PCT",
        "LYMp",
        "NEUTp",
        "LYMn",
        "NEUTn"
    ])

    data_scaled = scaler.transform(data)

    prediction = model.predict(data_scaled)

    probabilities = model.predict_proba(data_scaled)

    result = label_encoder.inverse_transform(prediction)

    st.success(f"Diagnóstico: {result[0]}")

    st.subheader("Probabilidades")

    for i, class_name in enumerate(label_encoder.classes_):
        st.write(
            f"{class_name}: {probabilities[0][i] * 100:.2f}%"
        )