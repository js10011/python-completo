import matplotlib.pyplot as plt
import random

# Geração de números aleatórios
random_numbers = [random.randint(1, 100) for _ in range(1000)]

# Construção do histograma
plt.hist(random_numbers, bins=10, edgecolor='black')

# Configuração do título e eixos
plt.title('Distribuição de números aleatórios')
plt.xlabel('Valores')
plt.ylabel('Frequência')

# Exibição do histograma
plt.show()