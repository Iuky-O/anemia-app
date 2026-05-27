import streamlit as st
from utils.anemia_descriptions import ANEMIA_INFO

st.title("📚 Guia Completo sobre Anemias")

st.markdown("""
Esta página apresenta explicações sobre:

- Tipos de anemia
- Sintomas
- Características laboratoriais
- Parâmetros hematológicos utilizados no sistema
""")

st.divider()

# ======================
# EXPLICAÇÃO DAS FEATURES
# ======================

st.header("🧪 Parâmetros Hematológicos")

FEATURES_INFO = {
    "HGB": "Quantidade de hemoglobina no sangue.",
    "PLT": "Quantidade de plaquetas.",
    "WBC": "Quantidade de glóbulos brancos.",
    "RBC": "Quantidade de glóbulos vermelhos.",
    "MCV": "Volume médio das hemácias.",
    "MCH": "Quantidade média de hemoglobina por hemácia.",
    "MCHC": "Concentração média de hemoglobina nas hemácias.",
    # "PDW": "Variação do tamanho das plaquetas.",
    # "PCT": "Marcador associado a infecções bacterianas.",
    # "LYMp": "Percentual de linfócitos.",
    # "NEUTp": "Percentual de neutrófilos.",
    # "LYMn": "Quantidade absoluta de linfócitos.",
    # "NEUTn": "Quantidade absoluta de neutrófilos."
}

for feature, description in FEATURES_INFO.items():

    with st.expander(f"🩸 {feature}"):
        st.write(description)

# ======================
# TIPOS DE ANEMIA
# ======================

st.divider()

st.header("🧬 Tipos de Anemia")

for anemia_name, info in ANEMIA_INFO.items():

    with st.expander(f"📖 {info['title']}"):

        st.subheader("Descrição")
        st.write(info["description"])

        st.subheader("Possíveis sintomas")

        for characteristic in info["characteristics"]:
            st.write(f"- {characteristic}")