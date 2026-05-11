import numpy as np
import matplotlib.pyplot as plt

# Geração de dados
uniform_data = np.random.uniform(0, 100, 500)
normal_data = np.random.normal(50, 5, 500)

# Construção dos histogramas
plt.hist(uniform_data, bins=15, alpha=0.6, label='Distribuição Uniforme')
plt.hist(normal_data, bins=15, alpha=0.6, label='Distribuição Normal')

# Configuração do gráfico
plt.legend()
plt.grid(True)

# Exibição do gráfico
plt.xlabel('Valor')
plt.ylabel('Frequência')
plt.title('Comparação de Distribuições')
plt.show()