import pandas as pd
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('clientes-v2-tratados.csv')
print(df.head())

#df = df.drop(['data', 'estado_civil', 'idade', 'salario', 'nivel_educacao', 'numero_filhos', 'area_atuacao'], axis=1)
df = df[['idade', 'salario']]

#Normalização - MinMaxScaler
scaler = MinMaxScaler()
df['idadeMinMaxScaler_01'] = scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler_01'] = scaler.fit_transform(df[['salario']])

scaler = MinMaxScaler()
df['idadeMinMaxScaler'] = scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler'] = scaler.fit_transform(df[['salario']])

min_max_scaler = MinMaxScaler(feature_range=(-1, 1))
df['idadeMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['salario']])

#Padronização - StandardScaler
scaler = StandardScaler()
df['idadeStandardScaler'] = scaler.fit_transform(df[['idade']])
df['salarioStandardScaler'] = scaler.fit_transform(df[['salario']])

#Padronização - RobustScaler
scaler = RobustScaler()
df['idadeRobustScaler'] = scaler.fit_transform(df[['idade']])
df['salarioRobustScaler'] = scaler.fit_transform(df[['salario']])

print(df.head(15))

print('MinMaxScaler (de 0 a 1):')
print("Idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std {:.4f}".format(
	df['idadeMinMaxScaler_01'].min(),
	df['idadeMinMaxScaler_01'].max(),
	df['idadeMinMaxScaler_01'].mean(),
	df['idadeMinMaxScaler_01'].std()
))
print("Salário - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std {:.4f}".format(
	df['salarioMinMaxScaler_01'].min(),
	df['salarioMinMaxScaler_01'].max(),
	df['salarioMinMaxScaler_01'].mean(),
	df['salarioMinMaxScaler_01'].std()
))

print('\nMinMaxScaler (de -1 a 1):')
print("Idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std {:.4f}".format(
	df['idadeMinMaxScaler_mm'].min(),
	df['idadeMinMaxScaler_mm'].max(),
	df['idadeMinMaxScaler_mm'].mean(),
	df['idadeMinMaxScaler_mm'].std()
))
print("Salário - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std {:.4f}".format(
	df['salarioMinMaxScaler'].min(),
	df['salarioMinMaxScaler'].max(),
	df['salarioMinMaxScaler'].mean(),
	df['salarioMinMaxScaler'].std()
))
print('\nStandardScaler (ajuste a média a 0 e o desvio padrão a 1')
print("Idade - Min: {:.4f} Max: {:.4f} Mean: {:.18f} Std {:.4f}".format(
	df['idadeStandardScaler'].min(),
	df['idadeStandardScaler'].max(),
	df['idadeStandardScaler'].mean(),
	df['idadeStandardScaler'].std()
))
print("Salário - Min: {:.4f} Max: {:.4f} Mean: {:.18f} Std {:.4f}".format(
	df['salarioStandardScaler'].min(),
	df['salarioStandardScaler'].max(),
	df['salarioStandardScaler'].mean(),
	df['salarioStandardScaler'].std()
))
print('\nRobustScaler (ajuste a mediana e o IQR:')
print("Idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std {:.4f}".format(
	df['idadeRobustScaler'].min(),
	df['idadeRobustScaler'].max(),
	df['idadeRobustScaler'].mean(),
	df['idadeRobustScaler'].std()
))
print("Salário - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std {:.4f}".format(
	df['salarioRobustScaler'].min(),
	df['salarioRobustScaler'].max(),
	df['salarioRobustScaler'].mean(),
	df['salarioRobustScaler'].std()
))

