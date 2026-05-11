import pandas as pd

# Criando dados de vendas para o ano de 2022
data_2022 = {
    'mês': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
            'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
    'valor das vendas': [10000, 15000, 20000, 25000, 30000, 35000, 
                         40000, 45000, 50000, 55000, 60000, 65000]
}

# Criando dados de vendas para o ano de 2023
data_2023 = {
    'mês': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
            'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
    'valor das vendas': [11000, 16000, 21000, 26000, 31000, 36000, 
                         41000, 46000, 51000, 56000, 61000, 66000]
}

# Criando DataFrame a partir dos dados de vendas
df_2022 = pd.DataFrame(data_2022)
df_2023 = pd.DataFrame(data_2023)

# Exportando dados para um arquivo Excel com duas planilhas
with pd.ExcelWriter('annual_sales.xlsx', engine='xlsxwriter') as writer:
    df_2022.to_excel(writer, sheet_name='Sales_2022', index=False)
    df_2023.to_excel(writer, sheet_name='Sales_2023', index=False)