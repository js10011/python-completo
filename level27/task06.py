import pandas as pd

# Carregar dados do arquivo Excel
file_path = 'financial_report.xlsx'
sheet_name = 'Operações'
column_name = 'Renda'

# Ler dados da aba especificada
data = pd.read_excel(file_path, sheet_name=sheet_name)

# Selecionar a coluna "Renda"
income_data = data[column_name]

# Calcular renda mínima, máxima e média
min_income = income_data.min()
max_income = income_data.max()
mean_income = income_data.mean()

# Exibir resultados na tela
print(f"Renda mínima: {min_income}")
print(f"Renda máxima: {max_income}")
print(f"Média de renda: {mean_income}")