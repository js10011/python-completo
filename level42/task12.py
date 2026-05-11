import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from plotly.subplots import make_subplots

# Exemplo de dados de vendas
data = {
    'Category': ['Electronics', 'Clothing', 'Groceries', 'Books'],
    'Sales': [4000, 3000, 2000, 1500],
    'Week': [1, 1, 2, 2]
}

df = pd.DataFrame(data)

# Criando gráfico de pizza para mostrar a proporção percentual de vendas
fig_pie = px.pie(df, values='Sales', names='Category', title='Vendas por Categoria')

# Criando histograma para mostrar a distribuição das vendas por semanas
fig_bar = px.bar(df, x='Week', y='Sales', color='Category', barmode='group', title='Distribuição Semanal de Vendas')

# Criando dashboard com dois gráficos
fig = make_subplots(rows=1, cols=2, subplot_titles=("Vendas por Categoria", "Distribuição Semanal de Vendas"))

fig.add_trace(
    go.Pie(labels=df['Category'], values=df['Sales']),
    row=1, col=1
)

fig.add_trace(
    go.Bar(x=df['Week'], y=df['Sales'], name='Sales', marker_color='indigo'),
    row=1, col=2
)

# Adicionando elementos interativos para seleção de categoria
fig.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    args=[{'visible': [True, False]}],
                    label='Gráfico de Pizza',
                    method='update'
                ),
                dict(
                    args=[{'visible': [False, True]}],
                    label='Histograma',
                    method='update'
                ),
                dict(
                    args=[{'visible': [True, True]}],
                    label='Ambos',
                    method='update'
                ),
            ]),
            direction="down",
            showactive=True,
            x=0.25,
            y=1.15
        )
    ]
)

fig.update_layout(height=600, width=1000, title_text="Dashboard de Vendas")

fig.show()