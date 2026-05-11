import pandas as pd

# Leitura de dados do arquivo Excel "students.xlsx"
df = pd.read_excel("students.xlsx")

# Exibição das primeiras cinco linhas de dados no formato DataFrame
print(df.head())

import pandas as pd

# Leitura de dados da planilha "Q1" no arquivo "sales_data.xlsx"
df = pd.read_excel("sales_data.xlsx", sheet_name="Q1")

# Exibição das primeiras dez linhas do DataFrame na tela
print(df.head(10))