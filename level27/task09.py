import pandas as pd

# Criamos dados para cada trimestre
data_first_quarter = {
    "Produto": ["Produto A", "Produto B", "Produto C"],
    "Quantidade": [100, 150, 200],
    "Lucro": [1000, 1500, 2000]
}

data_second_quarter = {
    "Produto": ["Produto D", "Produto E", "Produto F"],
    "Quantidade": [110, 160, 210],
    "Lucro": [1100, 1600, 2100]
}

data_third_quarter = {
    "Produto": ["Produto G", "Produto H", "Produto I"],
    "Quantidade": [120, 170, 220],
    "Lucro": [1200, 1700, 2200]
}

# Criamos DataFrame para cada trimestre
df_first_quarter = pd.DataFrame(data_first_quarter)
df_second_quarter = pd.DataFrame(data_second_quarter)
df_third_quarter = pd.DataFrame(data_third_quarter)

# Escrevemos DataFrames no arquivo Excel em diferentes planilhas
with pd.ExcelWriter('quarterly_sales.xlsx') as writer:
    df_first_quarter.to_excel(writer, sheet_name='Primeiro trimestre', index=False)
    df_second_quarter.to_excel(writer, sheet_name='Segundo trimestre', index=False)
    df_third_quarter.to_excel(writer, sheet_name='Terceiro trimestre', index=False)