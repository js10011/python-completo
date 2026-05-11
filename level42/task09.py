import plotly.express as px
import pandas as pd

# Criamos o DataFrame com dados de temperatura por dias da semana
data = {
    'Data': ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo'],
    'Temperatura': [20, 21, 19, 22, 18, 17, 21]
}

df = pd.DataFrame(data)

# Criamos o gráfico de linha interativo com Plotly
fig = px.line(df, x='Data', y='Temperatura', title='Temperatura por Dias da Semana')

# Exibimos o gráfico
fig.show()