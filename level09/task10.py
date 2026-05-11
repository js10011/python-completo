# Criamos um conjunto com os nomes das frutas
fruits = {"maçã", "banana", "laranja", "pêra", "pêssego"}

# Solicitamos ao usuário o nome da fruta para remover
fruit_to_remove = input("Digite o nome da fruta para remover: ")

# Removemos a fruta do conjunto, se existir
fruits.discard(fruit_to_remove)

# Exibimos o conjunto atualizado
print("Conjunto atualizado de frutas:", fruits)