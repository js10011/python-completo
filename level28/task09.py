import pandas as pd

# Criamos um DataFrame com 5 linhas, incluindo valores ausentes e duplicatas
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Bob'],
    'Age': [25, 30, None, 45, 30],
    'Department': ['HR', 'IT', 'Finance', None, 'IT']
}

df = pd.DataFrame(data)

# Removemos as linhas com valores vazios
df = df.dropna()

# Removemos duplicatas
df = df.drop_duplicates()

# Exibimos o DataFrame limpo
print(df)