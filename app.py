import streamlit as st

st.set_page_config(
    page_title="Anemia Classification AI",
    layout="wide"
)

st.title("🩸 Sistema Inteligente de Classificação de Anemia")

st.markdown("""
Sistema inteligente para classificação de tipos de anemia utilizando Machine Learning e visualização de dados.

O projeto utiliza parâmetros hematológicos obtidos de exames CBC (Complete Blood Count) para prever diferentes tipos de anemia através de algoritmos de classificação.

---
            
### Autores

- LETÍCIA JULIANA ROCHA DE SOUSA
- IUMY PIMENTEL FARIAS
- EDUARDO PATRICK DE LIMA SOUSA
- ANTÔNIO GABRIEL PEREIRA DO AMARAL

---

### 📚 Dataset

Base utilizada:

```
https://www.kaggle.com/datasets/ehababoelnaga/anemia-types-classification
```

---

### 🚀 Tecnologias Utilizadas

#### Backend / IA

* Python
* Scikit-learn
* Pandas
* NumPy
* Joblib

#### Dashboard e Interface

* Streamlit
* Plotly

#### Visualização de Dados

* Matplotlib
* Seaborn

---

### 🧠 Algoritmos Utilizados

O sistema compara diferentes algoritmos de classificação:

* KNN (K-Nearest Neighbors)
* SVM (Support Vector Machine)
* Redes Neurais

O melhor modelo é salvo automaticamente e utilizado pelo sistema inteligente.

---
            
""")