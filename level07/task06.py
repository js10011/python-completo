# Busca de string

# Escreva um programa que cria uma lista de 10 elementos.
# O programa pede ao usuário para inserir uma string e depois verifica se ela está na lista ou não.

# Escreva seu código aqui
lista = ["casa", "chave", "pais", "senha", "praia", "dinheiro", "poder", "vingança", "comida", "computação"]
busca = input("Qual palavra deseja saber se estar na lista? ")
if busca in lista:
    print("Elemento encontrado")
else:
    print("elemento nao encontrado")