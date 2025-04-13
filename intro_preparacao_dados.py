# Análise Exploratória de Dados (AED)
import pandas as pd  # Importa a biblioteca pandas, essencial para manipulação de dados

# Lê o arquivo CSV com os dados dos clientes
df = pd.read_csv('clientes-v2.csv')
pd.set_option('display.width', None)

# Mostra os 5 primeiros registros do DataFrame (visão inicial dos dados)
print(df.head().to_string())

# Mostra os 5 últimos registros (ver se o final do arquivo também está certinho)
print(df.tail().to_string())


# Converte a coluna 'data' para o tipo datetime, no formato dia/mês/ano
# Se encontrar erro, ele transforma em NaT (valores nulos de data)
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

# Mostra as informações gerais do DataFrame (número de entradas, tipos de dados, valores nulos, etc)
print('========== VERIFICAÇÃO INICIAL: ==========')
print(df.info())

# Conta quantos valores nulos tem em cada coluna
print('========== ANÁLISE DE DADOS NULOS ========== \n', df.isnull().sum())

# Mostra a porcentagem de valores nulos por coluna (para entender a gravidade do problema)
print('========== % DE DADOS NULOS ========== \n', df.isnull().mean() * 100)

# Remove todas as linhas que contêm qualquer valor nulo
df.dropna(inplace=True)

# Confirma se todos os nulos foram removidos (se o total de nulos for 0, missão cumprida!)
print('========== CONFIRMAR REMOÇÃO DE DADOS NULOS: ==========\n', df.isnull().sum().sum())

# Verifica se existem registros duplicados (linha exatamente igual a outra)
print('========== ANÁLISE DE DADOS DUPLICADOS: ========== \n', df.duplicated().sum())

# Conta quantos valores únicos existem em cada coluna (bom para ver variabilidade dos dados)
print('========== ANÁLISE DE DADOS ÚNICOS: ========== \n', df.nunique())

# Gera estatísticas descritivas das colunas numéricas (count, mean, std, min, max, etc)
print('========== ESTATÍSTICAS DOS DADOS: ========== \n', df.describe())

# Mantém apenas as colunas mais relevantes para a análise
df = df[['idade', 'data', 'estado', 'salario', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao']]

# Mostra os primeiros registros do DataFrame com as colunas selecionadas
print(df.head().to_string())

# Salva o DataFrame tratado em um novo arquivo CSV (sem o índice)
df.to_csv('clientes-v2-tratados.csv', index=False)
