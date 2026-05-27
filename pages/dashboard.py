import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/anemia_dataset_filtrado.csv")

st.title("📊 Dashboard")

# ======================
# MÉTRICAS
# ======================

col1, col2, col3 = st.columns(3)

col1.metric("Total de Pacientes", len(df))
col2.metric("Tipos de Anemia", df["Diagnosis"].nunique())
col3.metric("Média HGB", round(df["HGB"].mean(), 2))

# ======================
# DISTRIBUIÇÃO
# ======================

fig = px.histogram(
    df,
    x="Diagnosis",
    color="Diagnosis",
    title="Distribuição dos Diagnósticos"
)

st.plotly_chart(fig, use_container_width=True)

# ======================
# BOXPLOT
# ======================

fig2 = px.box(
    df,
    x="Diagnosis",
    y="HGB",
    color="Diagnosis",
    title="HGB por Tipo de Anemia"
)

st.plotly_chart(fig2, use_container_width=True)

# ======================
# CORRELAÇÃO
# ======================

corr = df.corr(numeric_only=True)

fig3 = px.imshow(
    corr,
    text_auto=True,
    title="Mapa de Correlação"
)

st.plotly_chart(fig3, use_container_width=True)