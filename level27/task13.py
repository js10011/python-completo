import pandas as pd

# Criamos o DataFrame com dados sobre os funcionários
data = {
    'Nome': ['Anna', 'Boris', 'Victor', 'Georgiy', 'Dmitriy'],
    'Departamento': ['Vendas', 'Marketing', 'Vendas', 'Desenvolvimento', 'Marketing'],
    'Salário': [70000, 60000, 80000, 75000, 65000]
}

df = pd.DataFrame(data)

# Ordenamos o DataFrame primeiro por departamento, depois por salário em ordem decrescente
sorted_df = df.sort_values(by=['Departamento', 'Salário'], ascending=[True, False])

# Exibimos o DataFrame ordenado na tela
print(sorted_df)