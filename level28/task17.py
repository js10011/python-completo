import pandas as pd

# Criamos dados sobre os funcionários
data = {
    'Nome': ['Ivan', 'Maria', 'Pedro', 'Ana'],
    'Cargo': ['Engenheiro', 'Marketing', 'Analista', 'Gerente'],
    'Departamento': ['Desenvolvimento', 'Marketing', 'Análise', 'Gestão']
}

# Criamos o DataFrame
df = pd.DataFrame(data)

# Exportamos o DataFrame para um arquivo Excel sem índices
df.to_excel('employees.xlsx', index=False)