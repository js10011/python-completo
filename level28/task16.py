import pandas as pd

# Criando DataFrame a partir do dicionário fornecido data
data = {
    'Produto': ['Laranja', 'Maçã', 'Banana', 'Laranja', 'Banana', 'Maçã'],
    'Mês': ['Janeiro', 'Janeiro', 'Janeiro', 'Fevereiro', 'Fevereiro', 'Fevereiro'],
    'Vendas': [150, 200, 250, 130, 180, 210],
    'Ano': [2023, 2023, 2023, 2024, 2024, 2024]
}
df = pd.DataFrame(data)

# Usando pivot_table para criar a tabela dinâmica
pivot_table = pd.pivot_table(
    df, 
    values='Vendas', 
    index=['Produto', 'Ano'], 
    columns='Mês', 
    aggfunc='sum',
    margins=True,  # Adicionando a linha "Total" para o valor total das vendas
    margins_name='Total'  # Nomeando a linha de totais
)

# Exibindo a tabela dinâmica resultante
print(pivot_table)