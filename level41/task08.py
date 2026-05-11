import matplotlib.pyplot as plt
import numpy as np

# Criando o array x de 0 a 2π com passo de 0.1
x = np.arange(0, 2 * np.pi, 0.1)

# Calculando os valores do seno e cosseno para o array x
y_sin = np.sin(x)
y_cos = np.cos(x)

# Construção dos gráficos de seno e cosseno
plt.plot(x, y_sin, label='sin(x)')
plt.plot(x, y_cos, label='cos(x)')

# Adição de legenda para distinguir os gráficos
plt.legend()

# Rotulação dos eixos
plt.xlabel('x')
plt.ylabel('y')

# Título do gráfico
plt.title('Gráficos de seno e cosseno')

# Exibição do gráfico
plt.show()