import plotly.express as px
import pandas as pd

# Dados de vendas para cada mês
sales_data = {
    'Mês': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
    'Vendas': [1200, 1500, 1700, 1800, 1600, 2000, 2100, 1900, 2300, 2200, 2500, 2700]
}

# Criação do DataFrame
df = pd.DataFrame(sales_data)

# Criação do gráfico de linha interativo
fig = px.line(df, x='Mês', y='Vendas', title='Vendas da empresa por mês')

# Garantir a função de zoom
fig.update_xaxes(rangeslider_visible=True)

# Exibição do gráfico
fig.show()