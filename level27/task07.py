import pandas as pd

# Criação de DataFrame com dados sobre estudantes
data = {
    'Nome do estudante': ['Ivanov', 'Petrov', 'Sidorov'],
    'Média de notas': [4.5, 3.7, 4.2]
}
df = pd.DataFrame(data)

# Gravação do DataFrame em arquivo Excel sem índices
df.to_excel('students.xlsx', index=False, sheet_name='Grupo 1')