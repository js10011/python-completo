# Quem quer mais?

# Escreva um programa que crie uma lista vazia, depois peça ao usuário 5 elementos e os adicione à lista usando o método append().
# Depois disso, o programa deve exibir a lista final.

# Escreva seu código aqui
lista =[]
for x in range(5):
    item = input("Insira um elemento: ")
    lista.append(item)
print(lista)