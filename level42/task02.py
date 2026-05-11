import matplotlib.pyplot as plt
import numpy as np

# Dados para o gráfico
x = np.arange(0, 6, 1)
y1 = np.square(x)
y2 = np.power(x, 3)

# Criação do gráfico
plt.figure()

# Primeira linha para o quadrado dos valores
plt.plot(x, y1, label='Quadrado', color='blue')

# Segunda linha para o cubo dos valores
plt.plot(x, y2, label='Cubo', color='green')

# Adicionando legenda
plt.legend()

# Configuração da cor dos eixos
plt.gca().spines['bottom'].set_color('red')
plt.gca().spines['left'].set_color('red')

# Adicionando grade
plt.grid(True)

# Configuração dos rótulos no eixo X
plt.xticks(np.arange(0, 6, 1))

# Nomes dos eixos
plt.xlabel('Valores')
plt.ylabel('Resultados')

# Mostrar gráfico
plt.show()