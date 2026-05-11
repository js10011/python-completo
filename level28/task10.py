import pandas as pd
import numpy as np

# Criamos o DataFrame com valores ausentes na coluna "Quantidade"
data = {
    'Produto': ['Produto1', 'Produto2', 'Produto3', 'Produto4', 'Produto5', 'Produto6', 'Produto7'],
    'Quantidade': [10, np.nan, 15, np.nan, 20, np.nan, 25]
}

df = pd.DataFrame(data)

# Calculamos a média da coluna "Quantidade"
average_quantity = df['Quantidade'].mean()

# Substituímos os valores ausentes pela média
df['Quantidade'].fillna(average_quantity, inplace=True)

# Exibimos o DataFrame formatado
print(df)