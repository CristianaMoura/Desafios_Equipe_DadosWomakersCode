import pandas as pd
from pydataset import data


## 1. Importe o dataset utilizando a seguinte função do pydataset: data(“Código”)
df = data('iris')

## 2. Imprimir na tela o dataset;
print(df)


## 3. Informe o tipo de dados retornado pela função data;
print(type(df))

## 4. Informe o número de exemplos (linhas) e características (colunas) do dataset.
print(df.shape)

## 5. Crie uma função que ao receber um DataFrame retorna o número de linhas e colunas.
def row_columns(df):
    return df.shape
print(row_columns(df))



