import matplotlib.pyplot as plt

# Dados
days = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
sales = [12, 19, 3, 5, 2, 3, 7]

# Criação do gráfico de barras
plt.bar(days, sales)

# Configuração dos rótulos dos eixos
plt.xlabel('Dias da semana')
plt.ylabel('Vendas')

# Adição de título
plt.title('Vendas da semana')

# Exibição do gráfico
plt.show()