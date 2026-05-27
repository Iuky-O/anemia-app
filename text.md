# Dataset de Classificação de Tipos de Anemia

Base utilizada:
https://www.kaggle.com/datasets/ehababoelnaga/anemia-types-classification

Este dataset utiliza parâmetros de hemograma completo (CBC — Complete Blood Count) para classificar diferentes tipos de anemia utilizando aprendizado de máquina.

---

# Objetivo do Dataset

O objetivo do dataset é prever o tipo de anemia de um paciente com base em exames laboratoriais do sangue.

A coluna alvo (`Diagnosis`) representa o tipo de anemia identificado.

---

# Campos do Dataset

## 1. HGB (Hemoglobin / Hemoglobina)

Quantidade de hemoglobina presente no sangue.

A hemoglobina transporta oxigênio pelo corpo.

### Interpretação

* Baixo → possível anemia
* Alto → possível desidratação

### Valores normais

* Homens: 13–17 g/dL
* Mulheres: 12–15 g/dL

---

## 2. PLT (Platelets / Plaquetas)

Quantidade de plaquetas no sangue.

As plaquetas ajudam na coagulação.

### Interpretação

* Baixo → risco de sangramento
* Alto → inflamações ou distúrbios hematológicos

---

## 3. WBC (White Blood Cells / Leucócitos)

Quantidade de glóbulos brancos.

Responsáveis pela defesa do organismo.

### Interpretação

* Alto → infecções ou inflamações
* Baixo → imunidade reduzida

---

## 4. RBC (Red Blood Cells / Hemácias)

Quantidade de glóbulos vermelhos.

Responsáveis pelo transporte de oxigênio.

### Interpretação

* Baixo → anemia
* Alto → desidratação ou policitemia

---

# Índices Hematimétricos

Os índices hematimétricos ajudam a identificar o tipo da anemia.

---

## 5. MCV (Mean Corpuscular Volume)

Volume médio das hemácias.

Indica o tamanho das células vermelhas.

### Interpretação

* Baixo → anemia microcítica
* Normal → anemia normocítica
* Alto → anemia macrocítica

---

## 6. MCH (Mean Corpuscular Hemoglobin)

Quantidade média de hemoglobina por hemácia.

### Interpretação

* Baixo → pouca hemoglobina nas células
* Alto → maior quantidade de hemoglobina

---

## 7. MCHC (Mean Corpuscular Hemoglobin Concentration)

Concentração média de hemoglobina nas hemácias.

### Interpretação

* Baixo → anemia ferropriva
* Alto → alterações hematológicas específicas

---

# Plaquetas e Inflamação

## 8. PDW (Platelet Distribution Width)

Mede a variação do tamanho das plaquetas.

### Interpretação

* Alto → produção irregular de plaquetas
* Pode indicar inflamação

---

## 9. PCT (Procalcitonin / Procalcitonina)

Marcador utilizado para detectar infecções bacterianas graves.

### Aplicações

* Sepse
* Infecções sistêmicas

### Interpretação

* Alto → forte suspeita de infecção bacteriana

---

# Linfócitos e Neutrófilos

## 10. LYMp

Percentual de linfócitos.

### Interpretação

* Alto → infecção viral
* Baixo → imunossupressão

---

## 11. NEUTp

Percentual de neutrófilos.

### Interpretação

* Alto → infecção bacteriana
* Baixo → neutropenia

---

## 12. LYMn

Quantidade absoluta de linfócitos.

Representa o número total de linfócitos no sangue.

---

## 13. NEUTn

Quantidade absoluta de neutrófilos.

Utilizado para avaliar resposta imunológica.

---

# Possíveis Resultados (Diagnosis)

A coluna `Diagnosis` representa o tipo de anemia identificado.

---

# 1. Iron Deficiency Anemia (IDA)

Anemia por deficiência de ferro.

É o tipo mais comum de anemia.

## Características

* HGB ↓
* RBC ↓
* MCV ↓
* MCH ↓
* MCHC ↓

## Sintomas

* Cansaço
* Fraqueza
* Palidez

---

# 2. Megaloblastic Anemia

Anemia causada principalmente por deficiência de:

* vitamina B12
* ácido fólico

## Características

* HGB ↓
* MCV ↑

## Efeito

As hemácias ficam maiores que o normal.

---

# 3. Normocytic Anemia

Anemia normocítica.

As hemácias possuem tamanho normal, porém em quantidade reduzida.

## Características

* HGB ↓
* MCV normal

## Possíveis causas

* Doenças crônicas
* Insuficiência renal
* Sangramentos

---

# 4. Microcytic Hypochromic Anemia

Anemia microcítica hipocrômica.

As hemácias tornam-se:

* pequenas
* com pouca hemoglobina

## Características

* MCV ↓
* MCH ↓
* MCHC ↓

---

# 5. Hemolytic Anemia

Anemia hemolítica.

Ocorre quando as hemácias são destruídas rapidamente.

## Características

* RBC ↓
* HGB ↓

## Possíveis causas

* Doenças autoimunes
* Infecções
* Alterações genéticas

---

# 6. Aplastic Anemia

Anemia aplástica.

A medula óssea reduz a produção de células sanguíneas.

## Características

* RBC ↓
* WBC ↓
* PLT ↓

---

# 7. Thalassemia

Talassemia.

Doença genética relacionada à produção de hemoglobina.

## Características

* MCV ↓
* HGB ↓

Pode se parecer com anemia ferropriva.

---

# 8. Healthy / Normal

Paciente saudável.

Os parâmetros permanecem dentro da faixa normal.

---

# Possíveis Abreviações no Dataset

| Nome Completo                 | Abreviação |
| ----------------------------- | ---------- |
| Iron Deficiency Anemia        | IDA        |
| Megaloblastic Anemia          | MA         |
| Normocytic Anemia             | NA         |
| Microcytic Hypochromic Anemia | MHA        |
| Hemolytic Anemia              | HA         |
| Aplastic Anemia               | AA         |
| Thalassemia                   | TH         |
| Healthy                       | Normal     |

---

# Como o Modelo Identifica os Tipos de Anemia

Os principais atributos utilizados são:

* HGB
* RBC
* MCV
* MCH
* MCHC

Esses parâmetros descrevem:

* quantidade de hemoglobina
* tamanho das hemácias
* concentração de hemoglobina

Com isso, o modelo consegue reconhecer padrões específicos de diferentes tipos de anemia.

---

# Resumo Geral

| Tipo de Anemia          | Principal Característica             |
| ----------------------- | ------------------------------------ |
| Ferropriva              | Deficiência de ferro                 |
| Megaloblástica          | Hemácias grandes                     |
| Normocítica             | Hemácias normais em baixa quantidade |
| Microcítica Hipocrômica | Hemácias pequenas e pálidas          |
| Hemolítica              | Destruição acelerada das hemácias    |
| Aplástica               | Falha da medula óssea                |
| Talassemia              | Alteração genética da hemoglobina    |
| Normal                  | Sem anemia                           |

---