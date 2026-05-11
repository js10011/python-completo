import numpy as np
import matplotlib.pyplot as plt

# Geração de 1000 números aleatórios normais com média 50 e desvio padrão 10
data = np.random.normal(50, 10, 1000)

# Construção do histograma
plt.hist(data, bins=20, color='red', edgecolor='black')

# Adição do título
plt.title("Histograma Ajustado da Distribuição Normal")

# Adição da grade
plt.grid(True)

# Exibição do histograma
plt.show()