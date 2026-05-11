import pandas as pd

# Criamos um DataFrame com dados sobre transações
data = {
    'Categoria': ['Alimentos', 'Alimentos', 'Roupas', 'Roupas', 'Eletrônicos', 'Eletrônicos'],
    'Valor da Transação': [150, 200, 500, 250, 400, 600],
    'Número de Transações': [1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

# Agrupamos os dados por 'Categoria' e calculamos as funções agregadas
grouped = df.groupby('Categoria').agg({
    'Valor da Transação': ['sum', 'mean', 'max']
})

# Exibimos os resultados
for category, row in grouped.iterrows():
    print(f"Categoria: {category}")
    print(f"  Soma: {row[('Valor da Transação', 'sum')]}")
    print(f"  Média: {row[('Valor da Transação', 'mean')]}")
    print(f"  Máximo: {row[('Valor da Transação', 'max')]}")
    print()