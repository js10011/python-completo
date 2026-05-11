import matplotlib.pyplot as plt

# Definição dos dados para os eixos
x_values = [1, 2, 3, 4, 5]
y_values = [3, 8, 1, 10, 5]

# Criação do gráfico de linha
plt.plot(x_values, y_values)

# Exibição do gráfico
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.title('Gráfico de Linha Simples')
plt.show()