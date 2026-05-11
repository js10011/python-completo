import matplotlib.pyplot as plt

# Criação de um array de valores para o eixo X (de 1 a 47)
x_values = list(range(1, 48))

# Criação de um array de valores para o eixo Y (array de 47 zeros)
y_values = [0] * 47

# Construção do gráfico
plt.plot(x_values, y_values)

# Nome do gráfico
plt.title('Mulheres Presidentes dos EUA')

# Rótulos dos eixos
plt.xlabel('Número do presidente')
plt.ylabel('Número de mulheres presidentes')

# Exibição do gráfico
plt.show()