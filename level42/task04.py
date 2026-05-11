import matplotlib.pyplot as plt

# Dados mensais de vendas para os produtos A e B
months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
sales_A = [150, 200, 250, 220, 300, 350, 400, 320, 290, 310, 330, 360]
sales_B = [180, 210, 260, 230, 310, 370, 420, 340, 300, 330, 350, 380]

# Criação do gráfico
plt.figure(figsize=(10, 5))
plt.plot(months, sales_A, marker='o', label='Produto A', color='blue')
plt.plot(months, sales_B, marker='o', label='Produto B', color='green')

# Adicionando rótulos de valores acima de cada ponto
for i in range(len(months)):
    plt.text(i, sales_A[i] + 10, str(sales_A[i]), ha='center', fontdict={'fontweight': 'bold', 'color': 'blue'})
    plt.text(i, sales_B[i] + 10, str(sales_B[i]), ha='center', fontdict={'fontweight': 'bold', 'color': 'green'})

# Determinando valores máximos e adicionando anotações com setas
max_A = max(sales_A)
max_B = max(sales_B)
max_index_A = sales_A.index(max_A)
max_index_B = sales_B.index(max_B)

plt.annotate(f'Máx: {max_A}', xy=(max_index_A, max_A), xytext=(max_index_A, max_A + 50),
             arrowprops=dict(facecolor='blue', shrink=0.05), fontsize=10, color='blue')

plt.annotate(f'Máx: {max_B}', xy=(max_index_B, max_B), xytext=(max_index_B, max_B + 50),
             arrowprops=dict(facecolor='green', shrink=0.05), fontsize=10, color='green')

# Configurando título e legenda
plt.title('Vendas dos produtos por mês', fontdict={'fontsize': 14, 'fontweight': 'bold'})
plt.xlabel('Meses', fontdict={'fontsize': 12})
plt.ylabel('Vendas', fontdict={'fontsize': 12})
plt.legend()

# Exportar gráfico em PNG
plt.savefig('sales_chart.png', format='png')

# Mostrar gráfico
plt.show()