import plotly.express as px
import pandas as pd

# Criação do DataFrame com dados de receitas e despesas mensais
data = {
    'Dia': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'Receitas': [2000, 2200, 2500, 2100, 2300, 2400, 2200, 2600, 2700, 2800, 
                 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 
                 3900, 4000, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800],
    'Despesas': [1500, 1600, 1550, 1650, 1500, 1600, 1700, 1800, 1750, 1700, 
                 1650, 1600, 1550, 1500, 1450, 1400, 1350, 1300, 1250, 1200, 
                 1150, 1100, 1050, 1000, 950, 900, 850, 800, 750, 700]
}

df = pd.DataFrame(data)

# Criação do gráfico de dispersão interativo com Plotly
fig = px.scatter(df, x='Receitas', y='Despesas', title='Receitas e Despesas por Dia do Mês')

# Mostrar o gráfico
fig.show()