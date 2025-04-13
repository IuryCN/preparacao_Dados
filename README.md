# 🧪 Análise Exploratória de Dados e Pré-processamento com Scalers

Este projeto tem como objetivo realizar uma análise exploratória de dados (AED) e aplicar diferentes técnicas de normalização e padronização em variáveis numéricas de um conjunto de dados de clientes.

## 🛠️ Etapas Realizadas

### 1. Carregamento e Preparação dos Dados

Utilizamos a biblioteca **pandas** para manipulação dos dados. As etapas incluíram:

- Leitura do arquivo `clientes-v2.csv`
- Conversão da coluna de data para o formato datetime
- Análise e remoção de valores nulos (`dropna`)
- Detecção de duplicatas
- Estatísticas descritivas iniciais
- Seleção de colunas relevantes para a análise

Após o tratamento, os dados limpos foram salvos no arquivo `clientes-v2-tratados.csv`.

### 2. Normalização e Padronização

Aplicamos três tipos de transformação nas colunas **idade** e **salário**, usando os scalers do `sklearn.preprocessing`:

#### 🔹 MinMaxScaler
- Escala os valores para o intervalo [0, 1] ou [-1, 1]
- Ideal quando os dados não possuem outliers extremos

#### 🔹 StandardScaler
- Centraliza os dados com média 0 e desvio padrão 1
- Útil para algoritmos sensíveis à variância dos dados (ex: SVM, PCA)

#### 🔹 RobustScaler
- Usa mediana e IQR (Intervalo Interquartil)
- Excelente para lidar com outliers sem perder a cabeça (nem os dados)

### 3. Estatísticas Pós-Transformação

Para cada transformação aplicada, foram exibidas:

- Valor mínimo
- Valor máximo
- Média
- Desvio padrão

Com isso, foi possível comparar a distribuição dos dados em cada tipo de escala.

---


