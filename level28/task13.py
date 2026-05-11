import pandas as pd

# Dados originais
data = {
    'Produto': ['Laranja', 'Maçã', 'Banana', 'Laranja', 'Banana', 'Maçã'],
    'Mês': ['Janeiro', 'Janeiro', 'Janeiro', 'Fevereiro', 'Fevereiro', 'Fevereiro'],
    'Vendas': [150, 200, 250, 130, 180, 210]
}

# Criação do DataFrame a partir dos dados
df = pd.DataFrame(data)

# Criação da tabela dinâmica
pivot_table = df.pivot_table(values='Vendas', index='Mês', columns='Produto', aggfunc='sum', fill_value=0)

# Exibição da tabela dinâmica
print(pivot_table)