#Questão 6 - Como identificar e tratar outliers
import pandas as pd #Importando a biblioteca pandas para manipulação de dados

df_dados = pd.Series([15, 16, 14, 15, 17, 16, 15, 14, 300, -50, 16, 15]) #Criando uma Series com os dados fornecidos

media = df_dados.mean()
desvio = df_dados.std()
limite_inferior = media - 2 * desvio
limite_superior = media + 2 * desvio

outliers = df_dados[(df_dados < limite_inferior) | (df_dados > limite_superior)]
print(f"Outliers método STD: {outliers.tolist()}")
#Podemos observar que o valor 300 está muito distante da média dos outros valores.
#O valor -50 é um outlier negativo, mas não é identificado pelo método do desvio padrão, 
#pois o valor extremo 300 aumenta a média e o desvio padrão, ampliando o intervalo de aceitação.
#Portanto, o único outlier identificado é o 300.

Q1 = df_dados.quantile(0.25)
Q3 = df_dados.quantile(0.75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliersIQR = df_dados[(df_dados < limite_inferior) | (df_dados > limite_superior)]
print(f"Outliers método IQR: {outliersIQR.tolist()}")
#O valor 300 e o -50 são identificado como outlier, por que estão fora dos limites calculados pelo método do IQR.
#Ambos os métodos são válidos, mas o método do IQR é mais sensível a valores extremos em distribuições assimétricas.
#Sendo assim o modo mais eficaz para identificar outliers neste conjunto de dados é o método do IQR.
#Para tratar os outliers, podemos optar por removê-los ou substituí-los pela média ou mediana dos dados.
#Nesse caso, os valores 300 e -50 podem ser removidos ou tratados, pois representam uma pequena parcela do conjunto de dados e podem distorcer a análise.
#________________________________________________________________________________________________________________________#

#Questão 7 - Como concatenar vários DataFrames (empilhando linhas ou colunas)
df_1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})
df_2 = pd.DataFrame({
    'B': [7, 8, 9],
    'C': [10, 11, 12]
})
#Empilhando por linhas (axis=0)
df_linhas = pd.concat([df_1, df_2], axis=0, ignore_index=True)
print(f"\nDataFrame concatenado por linhas: \n{df_linhas}")
#Empilhando por colunas (axis=1)
df_colunas = pd.concat([df_1, df_2], axis=1)
print(f"\nDataFrame concatenado por colunas: \n{df_colunas}")
#Quando empilhado por linhas, as colunas diferentes resultam em NaN onde os dados estão ausentes.
#E ao empilhar por colunas, as linhas são alinhadas pelo índice, o que pode resultar em duplicação de índices se os DataFrames originais tiverem índices iguais.
#________________________________________________________________________________________________________________________#

#Questão 8 - leitura de um arquivo CSV em um DataFrame e exibindo as primeiras linhas
import gdown #Biblioteca para baixar arquivos do Google Drive usando o ID do arquivo.

file_id = "1LPIaskunX9MEvcUQ-9JcnEjcKGiMdZFf"
gdown.download(id=file_id, output="dados.csv", quiet=True)

df = pd.read_csv("dados.csv") 
df.head()
print(f"\nExibindo as primeiras linhas do DataFrame: \n{df.head()}") #Foi utilizado o print pois ao utilizar abaixo o filtro de idade, o resultado do head() não é exibido, e o print exibe as primeiras linhas do DataFrame. 
#A função pd.read_csv() é usada para ler um arquivo CSV e criar um DataFrame a partir dos dados contidos no arquivo.
#O método .head() é utilizado para exibir as primeiras linhas do DataFrame, o Default é mostrar as 5 primeiras linhas,
#mas podemos especificar o número de linhas a serem exibidas, por exemplo, df.head(10) para mostrar as 10 primeiras linhas.
#________________________________________________________________________________________________________________________#

#Questão 9 - Filtrar um DataFrame com base em uma condição específica
info_age = df[df['idade'] <= 30]
print(f"Coluna idade com o filtro: {info_age}")
#O código "df[df['idade'] <= 30]" cria um novo DataFrame que contém apenas as linhas do DataFrame original onde a coluna 'idade' tem valores menor ou iguais a 30.
#Esse filtro cria um conjunto booleano que apresenta True e False para cada linha, assim filtrando quem tem idade menor ou igual a 30 e exibindo apenas onde a condição é verdadeira(True).
#________________________________________________________________________________________________________________________#

#Questão 10 - Como lidar com valores ausentes (NaN) em um DataFrame?
import numpy as np
data = {
    'A': [1, 2, np.nan, 4],
    'B': [np.nan, 2, 3, 4],
    'C': [1, np.nan, np.nan, 4]
    }
df_nan = pd.DataFrame(data)

print(f"\nDataFrame original com valores NaN: \n{df_nan}")
df_dropna = df_nan.dropna()
print(f"\nDataFrame após remover linhas com NaN: \n{df_dropna}")
df_fillna = df_nan.fillna(df_nan.mean())
print(f"\nDataFrame após substituir NaN pela média da coluna: \n{df_fillna}")
#O método dropna() remove todas as linhas que contêm pelo menos um valor NaN
#E o método fillna() foi usado para substituir os valores NaN por um valor especificado, neste caso, a média da coluna.
#Essas são duas abordagens comuns para lidar com valores ausentes em um DataFrame usando pandas.
#________________________________________________________________________________________________________________________#