import matplotlib.pyplot as plt

# Dados sobre a participação de mercado das empresas no ano atual
companies = ['Company A', 'Company B', 'Company C', 'Company D', 'Company E']
market_shares = [25, 20, 15, 10, 30]  # Percentual de participação de mercado

# Determinando o líder de mercado
max_share_index = market_shares.index(max(market_shares))
explode = [0.1 if i == max_share_index else 0 for i in range(len(market_shares))]

# Cores especiais para os setores
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'orange']

# Criação do gráfico de pizza
plt.figure(figsize=(8,8))
plt.pie(market_shares, explode=explode, labels=companies, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Participação de Mercado de Cinco Empresas de Tecnologia no Ano Atual')

# Salvamento do gráfico como imagem no formato PNG
plt.savefig('market_share_pie_chart.png', format='png')

# Mostrando o gráfico
plt.show()