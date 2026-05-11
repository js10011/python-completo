import pandas as pd

# Criamos DataFrame com datas no formato string e valores numéricos como texto
data = {
    'dates': ['01-01-2020', '15-08-2021', '23-11-2022'],
    'numbers': ['10', '20', '30']
}
df = pd.DataFrame(data)

# Convertendo a coluna de datas para o formato datetime
df['dates'] = pd.to_datetime(df['dates'], format='%d-%m-%Y')

# Convertendo a coluna de números em texto para formato numérico
df['numbers'] = pd.to_numeric(df['numbers'])

# Exibindo o DataFrame atualizado
print(df)