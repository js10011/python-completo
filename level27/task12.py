import pandas as pd

# Criação do DataFrame
data = {
    'nome do produto': ['maçãs', 'bananas', 'pepinos', 'peras', 'tomates'],
    'categoria': ['frutas', 'frutas', 'vegetais', 'frutas', 'vegetais'],
    'quantidade': [5, 15, 7, 12, 9],
    'preço': [50, 30, 20, 45, 25]
}

df = pd.DataFrame(data)

# Filtragem por categoria "frutas" e quantidade maior que 10
filtered_df = df[(df['categoria'] == 'frutas') & (df['quantidade'] > 10)]

# Exibição dos dados filtrados
print(filtered_df)