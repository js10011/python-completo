import plotly.express as px
import plotly.io as pio

# Dados para o gráfico
df = px.data.iris()

# Criamos um gráfico interativo
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species', title="Iris Dataset - Sepal Width vs Sepal Length")

# Salvamos o gráfico em formato HTML
pio.write_html(fig, file='scatter_plot.html', auto_open=False)