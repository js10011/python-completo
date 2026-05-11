import plotly.express as px
import plotly.io as pio

# Exemplo de dados para o gráfico (dados do Canadá)
data = px.data.gapminder().query("country == 'Canada'")

# Criando um gráfico de linha
fig = px.line(data, x='year', y='gdpPercap', title='PIB per capita no Canadá')

# Configuração dos parâmetros de exportação usando Kaleido
pio.kaleido.scope.default_width = 800  # Definindo a largura da imagem
pio.kaleido.scope.default_height = 400  # Definindo a altura da imagem

# Exportar gráfico para PNG
fig.write_image("gdp_percap_canada.png", format='png')

# Exportar gráfico para PDF
fig.write_image("gdp_percap_canada.pdf", format='pdf')