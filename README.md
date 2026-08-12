# 🩸 Anemia Classification AI

Sistema inteligente para classificação de tipos de anemia utilizando Machine Learning e visualização de dados.

O projeto utiliza parâmetros hematológicos obtidos de exames CBC (Complete Blood Count) para prever diferentes tipos de anemia através de algoritmos de classificação.

O sistema pode ser acessado em:

https://anemia-app-g4eiyxyu2xicef49hvsx2p.streamlit.app/Predi%C3%A7%C3%A3o

---

# 📚 Dataset

Base utilizada:

https://www.kaggle.com/datasets/ehababoelnaga/anemia-types-classification

---

# 🚀 Tecnologias Utilizadas

## Backend / IA

* Python
* Scikit-learn
* Pandas
* NumPy
* Joblib

## Dashboard e Interface

* Streamlit
* Plotly

## Visualização de Dados

* Matplotlib
* Seaborn

---

# 🧠 Algoritmos Utilizados

O sistema compara diferentes algoritmos de classificação:

* KNN (K-Nearest Neighbors)
* SVM (Support Vector Machine)
* Decision Tree (Árvore de Decisão)

O melhor modelo é salvo automaticamente e utilizado pelo sistema inteligente.

---

# 📂 Estrutura do Projeto

```txt
anemia-ai/
│
├── data/
│   └── anemia.csv
│
├── models/
│   ├── svm_model.pkl
│   ├── scaler.pkl
│   └── label_encoder.pkl
│
├── pages/
│   ├── dashboard.py
│   └── prediction.py
│
├── training/
│   └── train_model.py
│
├── utils/
│   └── helpers.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

# 📊 Funcionalidades

## Dashboard Analítico

* Distribuição dos diagnósticos
* Boxplots
* Heatmap de correlação
* Métricas da base

## Sistema Inteligente

* Predição de tipos de anemia
* Probabilidade da previsão
* Classificação em tempo real

## Comparação de Modelos

* Accuracy
* Precision
* Recall
* F1-score

---

# ⚙️ Como Rodar o Projeto

---

# 1. Clonar o Repositório

```bash
git clone <URL_DO_REPOSITORIO>
```

Entrar na pasta:

```bash
cd anemia-ai
```

---

# 2. Criar Ambiente Virtual (venv)

## Linux / Mac

```bash
python3 -m venv venv
```

Ativar:

```bash
source venv/bin/activate
```

---

## Windows

```bash
python -m venv venv
```

Ativar:

```bash
venv\Scripts\activate
```

---

# 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

---

# 4. Adicionar o Dataset

Coloque o arquivo CSV dentro da pasta:

```txt
data/anemia.csv
```

---

# 5. Treinar os Modelos

Executar:

```bash
python training/train_model.py
```

O sistema irá:

* treinar os algoritmos
* comparar os resultados
* salvar o melhor modelo automaticamente

Os arquivos gerados ficarão em:

```txt
models/
```

---

# 6. Executar o Sistema Web

```bash
streamlit run app.py
```

---

# 🌐 Acesso ao Sistema

Após executar o Streamlit:

```txt
http://localhost:8501
```

---

# 📈 Dashboard

A página de dashboard apresenta:

* Quantidade de pacientes
* Tipos de anemia
* Distribuição dos diagnósticos
* Correlação entre variáveis
* Boxplots dos parâmetros hematológicos

---

# 🤖 Predição Inteligente

A página de predição permite:

* Inserir parâmetros laboratoriais
* Classificar o tipo de anemia
* Visualizar probabilidade da previsão

---

# 🧪 Features Utilizadas

O sistema utiliza os seguintes parâmetros:

| Feature | Descrição                         |
| ------- | --------------------------------- |
| HGB     | Hemoglobina                       |
| PLT     | Plaquetas                         |
| WBC     | Leucócitos                        |
| RBC     | Hemácias                          |
| MCV     | Volume corpuscular médio          |
| MCH     | Hemoglobina corpuscular média     |
| MCHC    | Concentração média de hemoglobina |
| PDW     | Variação do tamanho das plaquetas |
| PCT     | Procalcitonina                    |
| LYMp    | Percentual de linfócitos          |
| NEUTp   | Percentual de neutrófilos         |
| LYMn    | Quantidade de linfócitos          |
| NEUTn   | Quantidade de neutrófilos         |

---

# 🧬 Possíveis Classificações

O sistema pode identificar:

* Iron Deficiency Anemia
* Megaloblastic Anemia
* Normocytic Anemia
* Microcytic Hypochromic Anemia
* Hemolytic Anemia
* Aplastic Anemia
* Thalassemia
* Healthy / Normal

---

# 📌 Melhorias Futuras

## Sistema

* Upload de CSV para classificação em lote
* Histórico de previsões
* Autenticação de usuários
* API REST

## Machine Learning

* Redes neurais
* XGBoost
* Random Forest
* Cross Validation
* Hyperparameter Tuning

## Dashboard

* Filtros interativos
* Gráficos avançados
* Análise temporal
* Exportação PDF

## Deploy

* Streamlit Cloud
* Docker
* AWS
* Render

---

# 📷 Demonstração Esperada

## Dashboard

* métricas
* gráficos
* análise exploratória

## Sistema Inteligente

Entrada:

* HGB
* RBC
* MCV
* etc.

Saída:

```txt
Predição: Iron Deficiency Anemia
Confiança: 94%
```

---

# 👨‍💻 Autores

Projeto desenvolvido para disciplina de Inteligência Artificial / Machine Learning.

---

# 📄 Licença

Projeto acadêmico para fins educacionais.
