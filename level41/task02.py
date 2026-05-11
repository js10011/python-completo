import matplotlib.pyplot as plt

# Preparação dos dados para os eixos X e Y
x = list(range(1, 48))  # Números de ordem dos presidentes de 1 a 47
y = [0] * 43 + [1] * 4  # 0 para os primeiros 43 presidentes e 1 para o 44 e subsequentes

# Construção do gráfico
plt.plot(x, y, marker='o')

# Definição do nome do gráfico e dos rótulos dos eixos
plt.title('Presidentes Negros dos EUA')
plt.xlabel('Número do Presidente')
plt.ylabel('Quantidade de Presidentes Negros')

# Exibição do gráfico
plt.show()