import pandas as pd

# Criação do DataFrame a partir do dicionário fornecido
data = {
    'Produto': ['Laranja', 'Maçã', 'Banana', 'Laranja', 'Banana', 'Maçã'],
    'Mês': ['Janeiro', 'Janeiro', 'Janeiro', 'Fevereiro', 'Fevereiro', 'Fevereiro'],
    'Vendas': [150, 200, 250, 130, 180, 210]
}

df = pd.DataFrame(data)

# Criação da tabela pivot com a média das vendas para cada produto em cada mês
mean_sales = df.pivot_table(values='Vendas', index='Mês', columns='Produto', aggfunc='mean')

# Criação da tabela pivot com a quantidade de unidades vendidas para cada produto em cada mês
count_sales = df.pivot_table(values='Vendas', index='Mês', columns='Produto', aggfunc='count')

# Exibição dos resultados
print("Média das vendas para cada produto em cada mês:")
print(mean_sales)
print("\nQuantidade de unidades vendidas para cada produto em cada mês:")
print(count_sales)