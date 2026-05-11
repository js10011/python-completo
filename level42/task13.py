import plotly.graph_objects as go

# Dados iniciais
days_of_week = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
water_levels = [2.5, 3.0, 3.5, 3.8, 3.2, 2.9, 3.1]

# Criação do gráfico de linha
fig = go.Figure()

# Adição de linha ao gráfico
fig.add_trace(go.Scatter(x=days_of_week, y=water_levels, mode='lines+markers', name='Nível da água'))

# Adição de título e rótulos dos eixos
fig.update_layout(
    title='Variação do nível da água no reservatório ao longo da semana',
    xaxis_title='Dias da semana',
    yaxis_title='Nível da água (m)'
)

# Mostrar gráfico interativo
fig.show()