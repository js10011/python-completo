import pandas as pd

# Leitura dos dados de dois arquivos Excel
file1 = 'data1.xlsx'
file2 = 'data2.xlsx'

# Ler arquivos Excel no DataFrame
df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)

# Combinação de DataFrames
combined_df = pd.concat([df1, df2], ignore_index=True)

# Exibição do DataFrame combinado
print(combined_df)