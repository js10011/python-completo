import matplotlib.pyplot as plt

# Dados para o gráfico
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
temperatures = [22, 24, 19, 23, 25, 29, 30]

# Criação do gráfico de linha
plt.plot(days, temperatures, color='blue', linestyle='-.', marker='s', label='Temperature')

# Configuração de títulos e rótulos
plt.title("Weekly Temperature Changes")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")

# Adição da legenda
plt.legend()

# Ativação da grade
plt.grid(True)

# Salvamento do gráfico como imagem
plt.savefig("temperature_chart.png")

# Exibição do gráfico
plt.show()