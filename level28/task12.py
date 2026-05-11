import pandas as pd

# Carregar dados do Excel
input_file = 'transactions.xlsx'
output_file = 'cleaned_transactions.xlsx'
df = pd.read_excel(input_file, engine='openpyxl')

# Quantidade inicial de linhas
initial_row_count = len(df)

# Remover linhas onde faltam valores chave (por exemplo, transaction_id, customer_id, date)
df.dropna(subset=['transaction_id', 'customer_id', 'date'], inplace=True)

# Remover duplicatas
df.drop_duplicates(inplace=True)

# Converter a coluna de datas para o formato 'yyyy-mm-dd'
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.strftime('%Y-%m-%d')

# Converter a coluna 'amount' para formato numérico ignorando linhas que não podem ser convertidas
if 'amount' in df.columns:
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

# Remover linhas com lacunas restantes após as conversões
df.dropna(inplace=True)

# Calcular a quantidade de linhas removidas
cleaned_row_count = len(df)
removed_rows = initial_row_count - cleaned_row_count

# Salvar os dados limpos e formatados em um novo arquivo Excel
df.to_excel(output_file, index=False, engine='openpyxl')

# Exibir informações sobre a quantidade de linhas removidas
print(f"Quantidade de linhas removidas: {removed_rows}")

# Exibir informações sobre os tipos de dados de cada coluna após a limpeza
print("Tipos de dados de cada coluna após a limpeza:")
print(df.dtypes)