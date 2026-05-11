import pandas as pd

# Dados de vendas na forma de uma lista de dicionários
sales_data = [
    {'data': '2023-10-01', 'produto': 'Produto A', 'valor': 2500},
    {'data': '2023-10-02', 'produto': 'Produto B', 'valor': 1500},
    {'data': '2023-10-03', 'produto': 'Produto C', 'valor': 3000},
    {'data': '2023-10-04', 'produto': 'Produto A', 'valor': 1000},
    {'data': '2023-10-05', 'produto': 'Produto B', 'valor': 2000},
    {'data': '2023-10-06', 'produto': 'Produto C', 'valor': 3500},
    # Adicione mais dados conforme necessário
]

# Criação do DataFrame a partir da lista de dicionários
df = pd.DataFrame(sales_data)

# Exportação do DataFrame para um arquivo Excel
excel_filename = 'sales_report.xlsx'
df.to_excel(excel_filename, index=False)

print(f"Relatório de vendas salvo com sucesso no arquivo: {excel_filename}")