import matplotlib.pyplot as plt

# Dados para o gráfico
x_data = [0, 1, 2, 3, 4, 5]
y_data = [0, 1, 4, 9, 16, 25]

# Criação do gráfico
plt.plot(x_data, y_data, linestyle='--', color='red', marker='o')

# Configuração do título e rótulos dos eixos
plt.title("Sample Line Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Exibição do gráfico
plt.show()