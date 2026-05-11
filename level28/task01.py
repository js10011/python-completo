import pandas as pd  

# Criamos o DataFrame com informações sobre os produtos  
data = {  
    'Categoria': ['Produtos', 'Limpeza', 'Produtos', 'Roupas', 'Roupas'],  
    'Preço': [120, 300, 150, 500, 400],  
    'Quantidade': [1, 2, 3, 1, 2]  
}  

df = pd.DataFrame(data)  

# Agrupamos os dados por categoria e calculamos o preço total dos produtos  
total_price_per_category = df.groupby('Categoria')['Preço'].sum()  

# Exibimos os resultados  
print(total_price_per_category)