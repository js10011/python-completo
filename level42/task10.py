import plotly.graph_objects as go
import pandas as pd

# Exemplo de dados do exercício anterior
# Suponha que no exercício anterior foram usados séries temporais com datas e valores
data = {
    'date': pd.date_range(start='2021-01-01', periods=100, freq='D'),
    'value': pd.Series(range(100)) + (pd.Series(range(100)) * 0.1).cumsum()
}

# Converter os dados em DataFrame
df = pd.DataFrame(data)

# Criar a figura com Plotly
fig = go.Figure()

# Adicionar linha no gráfico
fig.add_trace(go.Scatter(x=df['date'], y=df['value'], mode='lines', name='Value'))

# Configurar eixos
fig.update_layout(
    title='Gráfico interativo com possibilidade de zoom e pan',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1, label='1m', step='month', stepmode='backward'),
                dict(count=6, label='6m', step='month', stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(visible=True),
        type='date'
    ),
    yaxis=dict(title='Value'),
)

# Adicionar possibilidade de zoom e pan
fig.update_xaxes(rangeslider_visible=True)
fig.update_yaxes(fixedrange=False)  # O eixo Y também pode ser feito interativo

# Mostrar gráfico
fig.show()