import matplotlib.pyplot as plt

# Dados para o gráfico
x_values = list(range(6))
y_values = [x**2 for x in x_values]

# Criação do gráfico linear
plt.plot(x_values, y_values, marker='o')

# Anotação dos eixos
plt.xlabel('Número', fontsize=10, fontfamily='serif')
plt.ylabel('Quadrado do número', fontsize=10, fontfamily='serif')

# Configuração do título
plt.title('Quadrado dos números', fontsize=14, fontweight='bold')

# Exibição do gráfico
plt.grid(True)
plt.show()