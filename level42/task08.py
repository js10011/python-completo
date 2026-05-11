import numpy as np
import matplotlib.pyplot as plt

# Geração de dados
x = np.linspace(0, 2 * np.pi, 1000)
y = np.sin(x)

# Criação do gráfico
fig, ax = plt.subplots()
ax.plot(x, y)

# Remoção de bordas
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

# Salvar gráfico no formato SVG
fig.savefig("sine_wave.svg", format='svg', bbox_inches='tight', pad_inches=0)

# Salvar gráfico no formato JPEG
fig.savefig("sine_wave.jpg", format='jpeg', quality=95, bbox_inches='tight', pad_inches=0)

# Fechar gráfico
plt.close(fig)