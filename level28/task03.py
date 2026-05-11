import pandas as pd

# Criando DataFrame com dados de vendas
data = {
    'Loja': ['Loja A', 'Loja A', 'Loja B', 'Loja C', 'Loja C', 'Loja B', 'Loja A'],
    'Categoria': ['Eletrônicos', 'Roupas', 'Roupas', 'Eletrônicos', 'Roupas', 'Eletrônicos', 'Roupas'],
    'Receita': [200, 150, 300, 400, 200, 500, 100]
}

df = pd.DataFrame(data)

# Agrupando dados pelas colunas 'Loja' e 'Categoria'
grouped = df.groupby(['Loja', 'Categoria']).agg({
    'Receita': ['sum', 'mean']
}).reset_index()

# Renomeando colunas para melhor leitura
grouped.columns = ['Loja', 'Categoria', 'Receita Total', 'Receita Média']

# Exibindo resultados do agrupamento na tela
print(grouped)