import matplotlib.pyplot as plt

# Dados para a primeira linha
x1 = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]

# Dados para a segunda linha
x2 = [1, 2, 3, 4, 5]
y2 = [2, 4, 6, 8, 10]

# Criação do gráfico
plt.plot(x1, y1, label='Series A')  # Primeira linha com rótulo
plt.plot(x2, y2, label='Series B')  # Segunda linha com rótulo

# Adição de legenda
plt.legend()

# Exibição do gráfico
plt.show()