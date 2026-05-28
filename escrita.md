# Sistema Inteligente de Classificação de Anemia

**UNIVERSIDADE DO ESTADO DO PARÁ**  
CENTRO DE CIÊNCIAS NATURAIS E TECNOLOGIA  
CURSO DE BACHARELADO EM ENGENHARIA DE SOFTWARE

---

## Autores

- LETÍCIA JULIANA ROCHA DE SOUSA
- IUMY PIMENTEL FARIAS
- EDUARDO PATRICK DE LIMA SOUSA
- ANTÔNIO GABRIEL PEREIRA DO AMARAL

**Trabalho Final - Mineração de Dados**

Castanhal - PA, 2026

---

## Sumário

1. [Introdução](#1-introdução)
2. [Objetivos](#2-objetivos)
3. [Referencial Teórico](#3-referencial-teórico)
4. [Metodologia](#4-metodologia)
5. [Desenvolvimento do Sistema](#5-desenvolvimento-do-sistema)
6. [Resultados](#6-resultados)
7. [Conclusão](#7-conclusão)
8. [Referências](#referências)

---

## 1. Introdução

A anemia é uma das condições hematológicas mais prevalentes no mundo, afetando mais de 1,6 bilhão de pessoas, segundo estimativas da Organização Mundial da Saúde (OMS). Caracterizada pela redução da quantidade de hemoglobina ou de glóbulos vermelhos no sangue, a anemia pode ter origens distintas: carenciais, hereditárias, autoimunes ou relacionadas a doenças crônicas, o que torna seu diagnóstico diferencial um desafio clínico relevante.

O diagnóstico preciso do tipo de anemia é determinante para a conduta terapêutica adequada. Exames laboratoriais como o hemograma completo (Complete Blood Count — CBC) fornecem um conjunto rico de parâmetros hematológicos que, quando interpretados em conjunto, permitem distinguir diferentes formas da doença. Entre os parâmetros mais relevantes estão a hemoglobina (HGB), a contagem de hemácias (RBC), o volume corpuscular médio (MCV), a hemoglobina corpuscular média (MCH), a concentração de hemoglobina corpuscular média (MCHC), as plaquetas (PLT) e os leucócitos (WBC).

O avanço das técnicas de aprendizado de máquina (Machine Learning) tem aberto novas perspectivas para o auxílio ao diagnóstico médico. Algoritmos de classificação são capazes de aprender padrões complexos a partir de dados laboratoriais e generalizar esse conhecimento para novos pacientes, contribuindo para diagnósticos mais rápidos e consistentes, especialmente em contextos em que o acesso a especialistas é limitado.

Nesse contexto, o presente trabalho propõe o desenvolvimento de um sistema inteligente de classificação de tipos de anemia, utilizando dados de hemograma extraídos de uma base pública disponibilizada no Kaggle. O sistema integra análise exploratória dos dados, pré-processamento, comparação entre múltiplos algoritmos de classificação e uma interface web interativa com dashboard analítico e módulo de predição em tempo real.

---

## 2. Objetivos

### 2.1 Objetivo Geral

Desenvolver um sistema inteligente de classificação de tipos de anemia baseado em parâmetros hematológicos de hemograma, integrando análise exploratória de dados, comparação de algoritmos de aprendizado de máquina e uma interface web interativa para predição e visualização.

### 2.2 Objetivos Específicos

- Selecionar e explorar uma base de dados pública de hemograma adequada ao problema de classificação de anemia;
- Realizar limpeza, organização e análise exploratória dos dados (EDA), identificando distribuições, correlações e desbalanceamentos de classes;
- Implementar e comparar o desempenho de pelo menos três algoritmos de classificação: K-Nearest Neighbors (KNN), Support Vector Machine (SVM) e Redes Neurais, com uso de validação cruzada;
- Aplicar técnicas de balanceamento de classes (SMOTE) para mitigar o desbalanceamento na base de dados;
- Selecionar o modelo com melhor desempenho e integrá-lo a um sistema web desenvolvido com Streamlit;
- Construir um dashboard analítico com visualizações interativas dos parâmetros hematológicos;
- Disponibilizar um módulo de predição em tempo real, permitindo que o usuário informe os valores do hemograma e obtenha o diagnóstico estimado com a probabilidade associada.

---

## 3. Referencial Teórico

### 3.1 Anemia: conceito e classificação

A anemia é definida pela OMS como a condição em que o número de hemácias ou a concentração de hemoglobina é insuficiente para satisfazer as necessidades fisiológicas do organismo. Do ponto de vista morfológico, pode ser classificada em microcítica (MCV reduzido), normocítica (MCV normal) ou macrocítica (MCV elevado). Do ponto de vista etiológico, as formas mais relevantes incluem anemia ferropriva, anemia megaloblástica, anemia hemolítica, anemia aplástica, talassemia e anemia normocítica (FAILACE, 2015).

O hemograma completo é o exame de rastreamento primário para a investigação das anemias. Os índices hematimétricos — MCV, MCH e MCHC — em conjunto com os valores absolutos de HGB, RBC, PLT e WBC, formam uma assinatura laboratorial característica para cada subtipo, o que viabiliza a abordagem de classificação automática.

### 3.2 Aprendizado de Máquina para Diagnóstico

O aprendizado de máquina supervisionado consiste em induzir um modelo preditivo a partir de exemplos rotulados, de modo que o modelo generalize seu aprendizado para instâncias não vistas (MITCHELL, 1997). No contexto médico, essa abordagem tem sido amplamente aplicada para classificação de patologias, triagem de exames e apoio à decisão clínica.

Entre os algoritmos mais utilizados em problemas de classificação clínica estão o KNN, pelo seu caráter não paramétrico e intuitivo; o SVM, pela sua eficácia em espaços de alta dimensionalidade e pelo uso de kernels para separação não linear; e Redes Neurais Artificiais (MLP), pela sua capacidade de aprender representações complexas. Redes neurais, embora poderosas, exigem volumes maiores de dados para generalização adequada.

### 3.3 K-Nearest Neighbors (KNN)

O KNN é um classificador baseado em instâncias que atribui a uma nova amostra a classe majoritária dentre seus k vizinhos mais próximos no espaço de features, segundo alguma métrica de distância — tipicamente a distância euclidiana. É sensível à escala das variáveis, exigindo normalização prévia, e à escolha do hiperparâmetro k. Diferentes valores de k foram testados neste trabalho para otimização do modelo.

### 3.4 Support Vector Machine (SVM)

O SVM busca o hiperplano de margem máxima que separa as classes no espaço de features. Por meio do kernel trick, é possível mapear os dados para espaços de maior dimensão, viabilizando a separação não-linear (PEDREGOSA et al., 2011). Kernels lineares, polinomiais e RBF (Radial Basis Function) foram explorados neste trabalho, com a seleção automática de hiperparâmetros via GridSearchCV.

### 3.5 Rede Neural Artificial (MLP)

Redes neurais artificiais do tipo Multilayer Perceptron (MLP) são compostas por camadas de neurônios artificiais com funções de ativação não-lineares. Este tipo de arquitetura é especialmente útil para problemas de classificação multiclasse (CHOLLET et al., 2015). O modelo implementado utilizou múltiplas camadas densas com ativação ReLU nas camadas intermediárias e softmax na camada de saída para classificação multiclasse de 9 tipos de anemia. Foram empregadas técnicas de regularização como BatchNormalization, Dropout, EarlyStopping e ReduceLROnPlateau para evitar overfitting e melhorar a convergência.

### 3.6 SMOTE — Synthetic Minority Over-sampling Technique

O desbalanceamento de classes é um problema frequente em bases de dados médicas, onde determinadas condições são naturalmente mais raras. O SMOTE gera amostras sintéticas para as classes minoritárias por interpolação entre instâncias reais, contribuindo para um treinamento mais equilibrado sem descarte de dados da classe majoritária. Foi aplicado exclusivamente aos dados de treino dentro de cada fold de validação cruzada, evitando vazamento de dados.

---

## 4. Metodologia

### 4.1 Base de Dados

A base de dados utilizada é o conjunto "Anemia Types Classification" (ABOELNAGA, 2023), disponibilizado publicamente na plataforma Kaggle. A base contém registros de hemograma de pacientes com diferentes diagnósticos de anemia e indivíduos saudáveis, abrangendo 9 classes de diagnóstico: Anemia Ferropriva, Anemia Megaloblástica, Anemia Normocítica, Anemia Microcítica Hipocrômica, Anemia Hemolítica, Anemia Aplástica, Talassemia, além de pacientes classificados como saudáveis.

Do conjunto completo de variáveis disponíveis, foram selecionadas 7 features e o atributo alvo, conforme apresentado na Tabela 1.

**Tabela 1 — Variáveis selecionadas do hemograma**

| Variável | Descrição |
|----------|-----------|
| HGB | Hemoglobina — proteína das hemácias responsável pelo transporte de oxigênio |
| RBC | Eritrócitos (hemácias) — contagem de glóbulos vermelhos por mm³ |
| MCV | Volume Corpuscular Médio — tamanho médio das hemácias |
| MCH | Hemoglobina Corpuscular Média — quantidade de hemoglobina por hemácia |
| MCHC | Concentração de Hemoglobina Corpuscular Média |
| PLT | Plaquetas — células responsáveis pela coagulação sanguínea |
| WBC | Leucócitos — glóbulos brancos, células do sistema imunológico |
| Diagnosis | Rótulo alvo — tipo de anemia diagnosticado (9 classes) |

### 4.2 Pré-processamento

O pré-processamento dos dados compreendeu as seguintes etapas:

1. Seleção e filtragem das colunas relevantes;
2. Codificação da variável alvo Diagnosis por meio de LabelEncoder, convertendo os rótulos textuais em valores inteiros;
3. Normalização das features com StandardScaler (PEDREGOSA et al., 2011), aplicada em todo o conjunto para consistência;
4. Balanceamento das classes com SMOTE, aplicado exclusivamente aos dados de treinamento para evitar vazamento de informação.

### 4.3 Divisão e Validação dos Dados

A estratégia de avaliação dos modelos adotou validação cruzada com 5 folds estratificados, garantindo que a proporção de classes seja mantida em cada partição. Para os algoritmos de classificação (KNN e SVM), foi utilizado GridSearchCV com validação cruzada de 5 folds. A rede neural foi avaliada com divisão hold-out de 80% para treino e 20% para teste, com validação interna de 20% do conjunto de treinamento.

### 4.4 Métricas de Avaliação

Os modelos foram avaliados pelas métricas de acurácia média, precisão, revocação (recall) e F1-score, calculadas por meio do classification_report da biblioteca scikit-learn (PEDREGOSA et al., 2011). A matriz de confusão foi gerada para os melhores modelos, permitindo análise qualitativa dos erros de classificação por tipo de anemia.

---

## 5. Desenvolvimento do Sistema

### 5.1 Arquitetura Geral

O sistema desenvolvido, denominado **Anemia Classification AI**, é uma aplicação web construída em Python com o framework Streamlit, estruturada em módulos funcionais independentes. A arquitetura segue o padrão de separação de responsabilidades, com diretórios distintos para dados, modelos treinados, páginas da interface, utilitários e scripts de treinamento.

A aplicação é composta por dois módulos principais acessíveis pelo usuário:

- **Dashboard Analítico**: Visualizações e análise dos dados
- **Sistema Inteligente de Predição**: Predição em tempo real

Um terceiro módulo, de treinamento, opera em linha de comando e é responsável por treinar os classificadores, comparar seus resultados e persistir o melhor modelo em formato .pkl para uso pelo sistema web.

### 5.2 Pipeline de Treinamento

O script `training/train_model.py` implementa o pipeline completo de treinamento. Para cada algoritmo, os dados são submetidos à normalização via StandardScaler e balanceamento com SMOTE antes do ajuste (fit) do modelo. Ao final do processo, os modelos são comparados automaticamente por acurácia média de validação cruzada e o modelo com melhor desempenho é serializado com joblib, juntamente com o scaler e o label encoder, na pasta models/.

### 5.3 Dashboard Analítico

O módulo `pages/dashboard.py` apresenta as seguintes visualizações:

- Distribuição dos diagnósticos (gráfico de barras e pizza)
- Boxplots dos parâmetros hematológicos por tipo de anemia
- Heatmap de correlação entre variáveis
- Métricas gerais da base de dados (total de pacientes e contagem por classe)

As visualizações foram produzidas com as bibliotecas Plotly e Seaborn, garantindo interatividade e legibilidade.

### 5.4 Sistema Inteligente de Predição

O módulo `pages/prediction.py` disponibiliza uma interface de entrada onde o usuário informa os valores do hemograma (HGB, RBC, MCV, MCH, MCHC, PLT e WBC). Os valores são normalizados com o scaler salvo durante o treinamento e submetidos ao modelo SVM carregado. O sistema retorna o tipo de anemia previsto e a probabilidade associada à predição, utilizando o método predict_proba do classificador (PEDREGOSA et al., 2011).

### 5.5 Tecnologias Utilizadas

As principais tecnologias e bibliotecas empregadas no desenvolvimento foram:

- **Python 3.x** — linguagem principal do projeto
- **scikit-learn** (PEDREGOSA et al., 2011) — implementação dos algoritmos KNN e SVM, além de métricas de avaliação e pré-processamento
- **TensorFlow / Keras** (CHOLLET et al., 2015) — construção e treinamento da rede neural MLP
- **imbalanced-learn** — aplicação do SMOTE (CHAWLA et al., 2002) para balanceamento de classes
- **Pandas e NumPy** — manipulação e processamento de dados
- **Streamlit** (STREAMLIT INC., 2026) — framework para construção da interface web interativa
- **Plotly e Matplotlib/Seaborn** — visualizações estáticas e interativas
- **Joblib** — serialização e persistência dos modelos treinados
- **kagglehub** — download automatizado da base de dados via API do Kaggle

---

## 6. Resultados

### 6.1 Comparação dos Algoritmos

A avaliação inicial comparou três algoritmos de classificação distintos utilizando o script `training/train_model_advanced.py`. Todos os modelos foram treinados sobre os mesmos dados pré-processados com SMOTE, garantindo balanceamento das classes (1.935 amostras com distribuição equilibrada entre as 9 classes).

**Tabela 2 — Comparação de desempenho dos algoritmos na avaliação inicial**

| Algoritmo | Acurácia | Validação | Modelo Selecionado |
|-----------|----------|-----------|-------------------|
| KNN (k=5) | 78.60% | Cross-validation 5-fold | Não |
| SVM (kernel=rbf, C=100, γ=auto) | 88.72% | GridSearchCV 5-fold | **Sim ✓** |
| Rede Neural (MLP) | 82.88% | Hold-out 80/20 | Não |

*Fonte: execução de train_model_advanced.py (2026)*

O SVM obteve a melhor performance, sendo selecionado para otimização adicional. Os resultados detalhados do melhor modelo (SVM) na avaliação inicial são apresentados na Tabela 3.

**Tabela 3 — Relatório de classificação do SVM inicial (C=100, γ=auto)**

| Classe | Precisão | Recall | F1-Score | Suporte |
|--------|----------|--------|----------|---------|
| Healthy | 0.90 | 0.97 | 0.94 | 67 |
| Iron deficiency anemia | 0.89 | 0.84 | 0.86 | 38 |
| Leukemia | 0.67 | 0.44 | 0.53 | 9 |
| Leukemia with thrombocytopenia | 1.00 | 1.00 | 1.00 | 2 |
| Macrocytic anemia | 0.67 | 0.50 | 0.57 | 4 |
| Normocytic hypochromic anemia | 0.88 | 0.88 | 0.88 | 56 |
| Normocytic normochromic anemia | 0.91 | 0.98 | 0.95 | 54 |
| Other microcytic anemia | 0.73 | 0.67 | 0.70 | 12 |
| Thrombocytopenia | 1.00 | 0.87 | 0.93 | 15 |
| **Acurácia geral** | — | — | — | **0.89** |

*Fonte: train_model_advanced.py (2026)*

### 6.2 Otimização do Modelo SVM

Após a seleção do SVM como melhor modelo, foi executado o script `training/optimize_svm.py` com GridSearchCV abrangente para otimizar os hiperparâmetros. A busca explorou múltiplas combinações de parâmetros (kernel, C, gamma, class_weight e degree) com validação cruzada de 5 folds.

Os resultados da otimização identificaram os melhores parâmetros:
- **Kernel**: RBF
- **C**: 500
- **Gamma**: 0.1
- **Class_weight**: None
- **Degree**: 2

**Tabela 4 — Comparação: SVM inicial vs. SVM otimizado**

| Métrica | SVM Inicial | SVM Otimizado | Melhoria |
|---------|-------------|---------------|----------|
| CV Score | — | 97.88% | — |
| Acurácia no Teste | 88.72% | 90.27% | +1.55% |
| Acurácia Macro Avg | 85% | 91% | +6% |
| Acurácia Weighted Avg | 88% | 90% | +2% |

*Fonte: optimize_svm.py (2026)*

O modelo otimizado apresentou melhoria significativa, especialmente na capacidade de generalização (CV Score de 97.88%) e no tratamento de classes minoritárias, conforme evidenciado pela melhoria de 6% na macro-average.

**Tabela 5 — Relatório de classificação do SVM otimizado (C=500, γ=0.1)**

| Classe | Precisão | Recall | F1-Score | Suporte |
|--------|----------|--------|----------|---------|
| Healthy | 0.92 | 0.99 | 0.95 | 67 |
| Iron deficiency anemia | 0.91 | 0.84 | 0.88 | 38 |
| Leukemia | 0.80 | 0.44 | 0.57 | 9 |
| Leukemia with thrombocytopenia | 1.00 | 1.00 | 1.00 | 2 |
| Macrocytic anemia | 1.00 | 0.75 | 0.86 | 4 |
| Normocytic hypochromic anemia | 0.89 | 0.91 | 0.90 | 56 |
| Normocytic normochromic anemia | 0.88 | 0.98 | 0.93 | 54 |
| Other microcytic anemia | 0.80 | 0.67 | 0.73 | 12 |
| Thrombocytopenia | 1.00 | 0.87 | 0.93 | 15 |
| **Acurácia geral** | — | — | — | **0.90** |

*Fonte: optimize_svm.py (2026)*

### 6.3 Análise Comparativa

O KNN com k=5 alcançou 78.60% de acurácia, demonstrando desempenho moderado. A rede neural MLP, apesar de sua capacidade teórica, atingiu 82.88% — desempenho intermediário entre KNN e SVM. Este resultado reflete as limitações mencionadas em (CHOLLET et al., 2015): redes profundas requerem volumes maiores de dados para generalização adequada em problemas multiclasse com alta dimensionalidade.

O SVM inicial (88.72%) demonstrou capacidade superior de separação entre as classes. A otimização posterior elevou o modelo para 90.27%, representando uma melhoria robusta de 1.55 pontos percentuais. O modelo otimizado apresentou ganhos particularmente notáveis em classes minoritárias e em recall para diagnósticos críticos como Macrocytic anemia (melhoria de 25% em precisão).

---

## 7. Conclusão

### 7.1 Síntese dos Resultados

O presente trabalho alcançou com êxito seu objetivo ao desenvolver um sistema inteligente de classificação de tipos de anemia a partir de parâmetros hematológicos de hemograma. O processo envolveu desde a seleção e análise exploratória de uma base de dados real até a implementação, comparação e otimização de três algoritmos de classificação (KNN, SVM e Redes Neurais), seguido da construção de uma interface web interativa (STREAMLIT INC., 2026).

Os resultados confirmam a viabilidade do aprendizado de máquina para este problema diagnóstico. O SVM demonstrou ser a melhor escolha, combinando alta acurácia (90.27% após otimização) com capacidade de fornecer probabilidades de predição. O modelo otimizado com C=500, kernel RBF e γ=0.1 alcançou um CV Score de 97.88%, indicando excelente potencial de generalização.

A aplicação do SMOTE (CHAWLA et al., 2002) para balanceamento de classes foi determinante para mitigar o viés em direção às classes majoritárias, melhorando o F1-score das classes com menor representatividade, especialmente Anemia Aplástica, Talassemia e Leukemia.

### 7.2 Contribuições Técnicas

O sistema integra três componentes principais:

1. **Pipeline de Treinamento Robusto**: Implementação de validação cruzada estratificada com GridSearchCV, garantindo otimização sistemática de hiperparâmetros.

2. **Interface Interativa com Streamlit**: Acesso funcional e intuitivo sem exigência de conhecimento técnico por parte do usuário final, representando um diferencial para aplicações de apoio ao diagnóstico em ambientes clínicos.

3. **Dashboard Analítico**: Visualizações informativas para exploração dos dados hematológicos, facilitando a compreensão dos padrões de classificação.

### 7.3 Limitações e Perspectivas

Algumas classes minoritárias como Leukemia (recall de 44%) ainda apresentam desafio significativo. Este resultado está associado ao pequeno número de amostras de treinamento para estas categorias, apesar da aplicação de SMOTE.

O trabalho demonstra como técnicas de Mineração de Dados podem contribuir de forma concreta para o campo da saúde, aproximando o aprendizado de máquina de aplicações clínicas relevantes.

### 7.4 Trabalhos Futuros

Como trabalhos futuros, destacam-se:

1. **Expansão de Dados**: Incorporação de novos registros, especialmente para as classes menos representadas (Leukemia, Macrocytic anemia)
2. **Métodos Avançados**: Investigação de algoritmos de ensemble como XGBoost e Random Forest, que podem lidar melhor com desbalanceamento
3. **Funcionalidades Adicionais**: Implementação de upload de arquivo CSV para classificação em lote, permitindo diagnóstico em volume
4. **Implantação em Produção**: Publicação da aplicação em ambiente de nuvem (Streamlit Cloud, Render ou AWS) para acesso remoto
5. **Validação Clínica**: Avaliação do sistema com profissionais da saúde para validar utilidade prática em ambiente hospitalar
6. **Interpretabilidade**: Implementação de técnicas de explicabilidade (SHAP, LIME) para auxiliar profissionais na compreensão das predições

A otimização bem-sucedida do modelo SVM estabelece uma baseline robusta para futuras melhorias, enquanto a arquitetura modular do sistema facilita a incorporação de novos algoritmos e dados.

---

## Referências

ABOELNAGA, E. Anemia Types Classification Dataset. Kaggle, 2023. Disponível em: <https://www.kaggle.com/datasets/ehababoelnaga/anemia-types-classification>. Acesso em: maio 2026.

CHAWLA, N. V. et al. SMOTE: Synthetic Minority Over-sampling Technique. Journal of Artificial Intelligence Research, v. 16, p. 321–357, 2002. https://doi.org/10.1613/jair.953

CHOLLET, F. et al. Keras. GitHub, 2015. Disponível em: <https://github.com/keras-team/keras>. Acesso em: maio 2026.

FAILACE, R. et al. Hemograma: manual de interpretação. 5. ed. Porto Alegre: Artmed, 2015.

MITCHELL, T. M. Machine Learning. New York: McGraw-Hill, 1997.

ORGANIZAÇÃO MUNDIAL DA SAÚDE. Worldwide prevalence of anaemia 1993–2005: WHO Global Database on Anaemia. Geneva: WHO Press, 2008.

PEDREGOSA, F. et al. Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research, v. 12, p. 2825–2830, 2011.

STREAMLIT INC. Streamlit — The fastest way to build and share data apps. Disponível em: <https://streamlit.io>. Acesso em: maio 2026.
