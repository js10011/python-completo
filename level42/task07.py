import matplotlib.pyplot as plt
import numpy as np

# Criação dos dados
x = np.linspace(0, 10, 100)
y = x**2

# Construção do gráfico
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico da função y = x^2')
plt.legend()

# Salvando o gráfico em PDF com fundo transparente
plt.savefig('quadratic_graph.pdf', format='pdf', transparent=True)
plt.close()