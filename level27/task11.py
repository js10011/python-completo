import pandas as pd

# Criamos dados sobre os estudantes
data = {
    'Nome': ['Alexei', 'Maria', 'Ivan', 'Ana', 'Sergio'],
    'Idade': [19, 22, 21, 20, 23],
    'Média de Notas': [4.5, 4.0, 3.8, 4.2, 3.9]
}

# Criamos o DataFrame
df = pd.DataFrame(data)

# Filtramos os estudantes com mais de 20 anos
filtered_df = df[df['Idade'] > 20]

# Exibimos o DataFrame filtrado
print(filtered_df)