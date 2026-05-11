import matplotlib.pyplot as plt

# Dados para o gráfico de pizza
fruits = ['Maçãs', 'Bananas', 'Laranjas', 'Peras']
preferences = [30, 25, 20, 25]

# Construção do gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(preferences, labels=fruits, autopct='%1.1f%%', startangle=140)

# Adição do título
plt.title('Preferências de Frutas')

# Exibição do gráfico
plt.show()