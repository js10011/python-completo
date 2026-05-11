import plotly.express as px

# Dados sobre o número de visitantes no parque por dia da semana
data = {
    "Dia da Semana": ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"],
    "Número de Visitantes": [123, 150, 98, 170, 200, 230, 180]
}

# Criação do gráfico
fig = px.bar(data,
             x="Dia da Semana",
             y="Número de Visitantes",
             title="Número de Visitantes no Parque por Dia da Semana",
             labels={"Número de Visitantes": "Número de Visitantes"},
             color="Dia da Semana",  # Aplicação de esquema de cores
             hover_data={"Dia da Semana": True, "Número de Visitantes": True})  # Dicas flutuantes

# Exibição do gráfico
fig.show()