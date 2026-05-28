import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/anemia_dataset_filtrado.csv")

st.title("📊 Dashboard")

# ======================
# MÉTRICAS PRINCIPAIS
# ======================

col1, col2, col3 = st.columns(3)

col1.metric("Total de Pacientes", len(df))
col2.metric("Tipos de Anemia", df["Diagnosis"].nunique())
col3.metric("Média HGB - Hemoglobina", round(df["HGB"].mean(), 2))

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
    title="HGB (Hemoglobina) por Tipo de Anemia"
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

# ======================
# ESTATÍSTICAS DOS PARÂMETROS
# ======================

st.divider()

st.header("📈 Estatísticas dos Parâmetros Hematológicos")

# Colunas numéricas (excluindo a coluna de diagnóstico)
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns

# Criar um dicionário com as estatísticas
stats_data = []

for col in numeric_columns:
    stats_data.append({
        "Parâmetro": col,
        "Média": round(df[col].mean(), 2),
        "Mediana": round(df[col].median(), 2),
        "Min": round(df[col].min(), 2),
        "Max": round(df[col].max(), 2),
        "Desvio Padrão": round(df[col].std(), 2)
    })

stats_df = pd.DataFrame(stats_data)

# Mostrar a tabela de forma limpa
st.dataframe(stats_df, use_container_width=True, hide_index=True)
