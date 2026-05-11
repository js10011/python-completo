import matplotlib.pyplot as plt
import numpy as np

# Criando valores de x de 0 a 5
x = np.linspace(0, 5, 100)

# Calculando valores de y para três funções
y1 = x
y2 = x**2
y3 = x**3

# Criando o gráfico
plt.figure(figsize=(8, 6))

# Adicionando linhas ao gráfico
plt.plot(x, y1, label='y = x', color='blue', linestyle='-')  # Linha sólida
plt.plot(x, y2, label='y = x^2', color='green', linestyle='--')  # Linha tracejada
plt.plot(x, y3, label='y = x^3', color='red', linestyle=':')  # Linha pontilhada

# Configurando os eixos
plt.xlim(-1, 6)
plt.ylim(-1, 6)

# Adicionando anotação para o ponto de interseção (0, 0)
plt.annotate('Ponto de interseção\n(0, 0)', xy=(0, 0), xytext=(1, 1),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Adicionando legenda
plt.legend(loc='upper left', fontsize='medium', frameon=True, shadow=True)

# Adicionando rótulos dos eixos
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráficos y = x, y = x^2, y = x^3')

# Mostrando o gráfico
plt.grid(True)
plt.show()