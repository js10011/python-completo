# Criamos um dicionário com informações sobre o produto
product_info = {
    'Nome': 'Tomates',
    'Preço': 50,
    'Quantidade': 100
}

# Exibimos todos os pares chave-valor usando o método items()
for key, value in product_info.items():
    print(f"{key}: {value}")

print("\n")

# Iteramos sobre todos os pares chave-valor e os exibimos na tela
for key, value in product_info.items():
    print(f"{key}: {value}")

print("\n")

# Adicionamos um novo par chave-valor ao dicionário
product_info['Cor'] = 'Vermelho'

# Novamente exibimos todos os pares chave-valor
for key, value in product_info.items():
    print(f"{key}: {value}")