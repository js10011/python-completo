import matplotlib.pyplot as plt
import numpy as np

# Criação de dados para o gráfico
x = np.arange(0, 11)  # array x com valores de 0 a 10
y = x ** 2  # array y, igual ao quadrado de x

# Construção do gráfico linear
plt.plot(x, y)

# Rotulagem dos eixos e título do gráfico
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("Dependência Quadrática")

# Exibição do gráfico
plt.show()