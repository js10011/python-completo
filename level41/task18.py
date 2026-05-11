import matplotlib.pyplot as plt

# Dados sobre a participação de usuários de diferentes sistemas operacionais
labels = ['Windows', 'macOS', 'Linux', 'Other']
sizes = [45, 30, 15, 10]  # Valores de frações arbitrários
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']  # Cores únicas para cada categoria

# Calculando a maior participação para destacar o setor
max_index = sizes.index(max(sizes))
explode = [0] * len(sizes)
explode[max_index] = 0.1  # Destaque do setor com a maior participação

# Criação do gráfico de pizza
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

# Configurando eixos iguais para garantir a forma circular
plt.axis('equal')

# Exibição do gráfico na tela
plt.show()