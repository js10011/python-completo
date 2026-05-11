import pandas as pd

# Leitura de dados do arquivo Excel "employees.xlsx" especificando a planilha "Dados"
df = pd.read_excel('employees.xlsx', sheet_name='Dados')

# Filtragem de linhas onde o valor na coluna 'Idade' é maior que 30
filtered_df = df[df['Idade'] > 30]

# Exibição dos dados filtrados na tela
print(filtered_df)