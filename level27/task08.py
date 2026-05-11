import pandas as pd

# Criação do primeiro DataFrame com dados sobre produtos
products_data = {
    "Nome": ["Maçãs", "Bananas", "Laranjas"],
    "Preço": [100, 80, 90]
}
products_df = pd.DataFrame(products_data)

# Criação do segundo DataFrame com dados sobre clientes
customers_data = {
    "Nome": ["Alexandre", "Maria", "Ivan"],
    "Idade": [30, 25, 40]
}
customers_df = pd.DataFrame(customers_data)

# Gravação de ambos os DataFrames em um único arquivo Excel
with pd.ExcelWriter("market_data.xlsx") as writer:
    products_df.to_excel(writer, sheet_name='Produtos', index=False)
    customers_df.to_excel(writer, sheet_name='Clientes', index=False)