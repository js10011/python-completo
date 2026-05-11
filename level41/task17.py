import matplotlib.pyplot as plt

# Valores percentuais para cada categoria
percentages = [30, 25, 20, 25]
categories = ["Pizza", "Hambúrguer", "Sushi", "Massa"]

# Criação do gráfico de pizza
plt.pie(percentages, labels=categories, autopct='%1.1f%%', startangle=90)

# Garante que o gráfico tenha formato circular
plt.axis('equal')

# Exibição do gráfico
plt.title('Distribuição de preferências em comida favorita')
plt.show()