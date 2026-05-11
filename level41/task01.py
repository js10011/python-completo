import matplotlib.pyplot as plt

# Dados: número de dias por mês
days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Meses de 1 a 12
months = list(range(1, 13))

# Construção do gráfico
plt.plot(months, days_in_months, marker='o')

# Assinaturas dos eixos
plt.xlabel('Mês')
plt.ylabel('Número de dias')

# Título do gráfico
plt.title('Número de dias em cada mês')

# Exibição do gráfico
plt.grid(True)
plt.show()