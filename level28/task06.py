import pandas as pd

# Leitura de dados de todas as folhas do arquivo Excel
file_path = 'sales_data.xlsx'  # Especifique o caminho para o seu arquivo Excel
all_sheets_data = pd.read_excel(file_path, sheet_name=None)

# Unindo dados de todas as folhas em um único DataFrame
combined_data = pd.concat(all_sheets_data.values(), ignore_index=True)

# Exibição do DataFrame unido na tela
print(combined_data)