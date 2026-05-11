import pandas as pd
from random import randint

# Geração de dados de teste para temperatura e umidade
def generate_data():
    return {
        'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        'temperature_source_1': [randint(20, 30) for _ in range(7)],
        'humidity_source_1': [randint(50, 70) for _ in range(7)],
        'temperature_source_2': [randint(20, 30) for _ in range(7)],
        'humidity_source_2': [randint(50, 70) for _ in range(7)]
    }

# Combinação dos dados
def combine_data():
    data = generate_data()
    df = pd.DataFrame(data)
    return df

# Registro do DataFrame em Excel com folhas separadas por dias
def write_to_excel(df):
    with pd.ExcelWriter('climate_reports.xlsx') as writer:
        for day in df['day']:
            day_data = df[df['day'] == day]
            day_data.to_excel(writer, sheet_name=day, index=False)

# Código principal
df = combine_data()
write_to_excel(df)