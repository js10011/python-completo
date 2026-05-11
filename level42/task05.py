import matplotlib.pyplot as plt

# Dados para o gráfico
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Criação do gráfico linear
plt.plot(x, y)

# Definição do título e legendas dos eixos
plt.title('Simple Linear Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Salvando o gráfico como imagem no formato PNG
plt.savefig('simple_plot.png')

# Exibição do gráfico
plt.show()