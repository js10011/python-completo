import pandas as pd

# Leitura de dados de arquivos Excel
sales_data = pd.read_excel('sales.xlsx')
price_data = pd.read_excel('prices.xlsx')

# União de dados pela coluna "Product" usando o método "inner"
merged_data = pd.merge(sales_data, price_data, on='Product', how='inner')

# Exibição do DataFrame final na tela
print(merged_data)