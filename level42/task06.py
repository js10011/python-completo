import matplotlib.pyplot as plt

# Dados para o gráfico
y_values = [1, 4, 9, 16, 25]

# Criação do gráfico de linha
plt.plot(y_values)

# Removemos campos adicionais ao redor do gráfico
plt.axis('tight')

# Salvando o gráfico com os parâmetros especificados
plt.savefig("high_resolution_plot.png", dpi=150, bbox_inches='tight')
plt.close()