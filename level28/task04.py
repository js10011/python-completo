import pandas as pd  
import matplotlib.pyplot as plt  

# Exemplo de dados de vendas  
data = {  
    'Produto': ['Produto A', 'Produto B', 'Produto A', 'Produto C', 'Produto B', 'Produto C'],  
    'Região': ['Região 1', 'Região 2', 'Região 1', 'Região 2', 'Região 1', 'Região 2'],  
    'Vendas': [150, 200, 100, 300, 250, 400]  
}  

# Criando o DataFrame  
df = pd.DataFrame(data)  

# Agrupando os dados por 'Região' e 'Produto', calculando as vendas totais  
grouped_data = df.groupby(['Região', 'Produto'])['Vendas'].sum().unstack()  

# Criando o gráfico de barras  
grouped_data.plot(kind='bar', stacked=True)  

# Configurações do gráfico  
plt.title('Vendas totais de produtos por região')  
plt.xlabel('Região')  
plt.ylabel('Vendas totais')  
plt.legend(title='Produtos')  
plt.tight_layout()  

# Exibindo o gráfico na tela  
plt.show()