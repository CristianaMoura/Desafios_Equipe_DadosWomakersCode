import pandas as pd
from pydataset import data


# Importando o dataset
df = data('InsectSprays')
print(df)

total_mortos = df.groupby('spray')['count'].sum()

print(total_mortos)

total_mortos = df.groupby['spray']['count'].sum().idxmax()
print(total_mortos)

# 3. Calcule a média geral e filtre os dados para mostrar apenas sprays com eficácia acima da média.
media = df['count'].mean()
print(media)
