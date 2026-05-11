import plotly.express as px
import pandas as pd

# Criamos um exemplo de conjunto de dados
data = {
    'Temperatura': [15, 20, 25, 30, 35, 40, 20, 22, 18, 25, 30, 28],
    'Frequência': [100, 150, 200, 250, 300, 350, 160, 180, 190, 220, 260, 240],
    'Tipo de atração': ['Montanha Russa', 'Roda Gigante', 'Casa Assombrada', 'Toboágua', 
                        'Carrossel', 'Carrinhos de Bate-Bate', 'Montanha Russa', 'Roda Gigante', 
                        'Casa Assombrada', 'Toboágua', 'Carrossel', 'Carrinhos de Bate-Bate'],
    'Nível de Satisfação': [3.5, 4.0, 4.5, 4.8, 3.8, 4.2, 4.0, 4.1, 4.7, 4.9, 3.9, 4.3],
    'Mês': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 
            'Maio', 'Junho', 'Julho', 'Agosto', 
            'Setembro', 'Outubro', 'Novembro', 'Dezembro']
}

# Criamos o DataFrame
df = pd.DataFrame(data)

# Criamos o gráfico de dispersão interativo usando Plotly Express
fig = px.scatter(df, x='Temperatura', y='Frequência', 
                 hover_data=['Tipo de atração', 'Nível de Satisfação', 'Mês'],
                 title='Relação entre Temperatura e Frequência de Visitas a Atrações',
                 labels={'Temperatura': 'Temperatura (°C)', 'Frequência': 'Número de Visitantes'},
                 template='plotly')

# Adicionamos lasso select
fig.update_traces(marker=dict(size=10),
                  selector=dict(mode='markers'),
                  selected=dict(marker=dict(opacity=0.5)),
                  unselected=dict(marker=dict(opacity=1)),
                  mode='markers+text',
                  textposition='top center')

# Adicionamos a capacidade de seleção com a função "lasso select"
fig.update_layout(dragmode='lasso')

# Mostramos o gráfico
fig.show()