import plotly.express as px

# Usamos o conjunto de dados embutido iris do Plotly Express
df = px.data.iris()

# Criamos um gráfico interativo - Scatter plot
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species', title='Iris Dataset: Sepal Width vs Sepal Length')

# Exportamos o gráfico no formato HTML com auto_open=True
fig.write_html("interactive_plot.html", auto_open=True)