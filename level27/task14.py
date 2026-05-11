import pandas as pd

# Criando os dados sobre vendas de carros
data = {
    'Marca': ['Toyota', 'Ford', 'BMW', 'Mercedes', 'Honda'],
    'Modelo': ['Camry', 'Focus', 'X5', 'C-Class', 'Civic'],
    'Unidades Vendidas': [60, 30, 80, 45, 90],
    'Receita Gerada': [24000, 15000, 30000, 35000, 27000]
}

# Criando o DataFrame
df = pd.DataFrame(data)

# Filtrando os carros cuja quantidade de unidades vendidas seja maior que 50
filtered_df = df[df['Unidades Vendidas'] > 50]

# Ordenando o DataFrame filtrado pela receita em ordem crescente
sorted_filtered_df = filtered_df.sort_values(by='Receita Gerada')

# Exibindo o resultado na tela
print(sorted_filtered_df)