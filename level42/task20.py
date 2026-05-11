import plotly.express as px
import pandas as pd

# Exemplo de dados
data = {'Category': ['A', 'B', 'C', 'D'],
        'Values': [23, 45, 56, 78]}

# Criação do DataFrame
df = pd.DataFrame(data)

# Criação do gráfico linear
line_fig = px.line(df, x='Category', y='Values', title='Gráfico Linear')

# Criação do gráfico de barras
bar_fig = px.bar(df, x='Category', y='Values', title='Gráfico de Barras')

# Exportação dos gráficos para HTML
line_fig.write_html('line_chart.html', include_plotlyjs='cdn')
bar_fig.write_html('bar_chart.html', include_plotlyjs='cdn')