import pandas as pd

# Criamos o DataFrame com base nos dados de vendas
data = {
    'Produto': ['Laranja', 'Maçã', 'Banana', 'Laranja', 'Banana', 'Maçã'],
    'Mês': ['Janeiro', 'Janeiro', 'Janeiro', 'Fevereiro', 'Fevereiro', 'Fevereiro'],
    'Vendas': [150, 200, 250, 130, 180, 210]
}

df = pd.DataFrame(data)

# Usamos o crosstab para calcular o total de vendas por produtos e meses
result = pd.crosstab(index=df['Produto'], columns=df['Mês'], values=df['Vendas'], aggfunc='sum')

# Exibimos a tabela na tela
print(result)