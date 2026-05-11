# Lista única.

# Escreva um programa que crie uma lista de 10 elementos solicitados ao usuário.
# Em seguida, o programa deve criar um conjunto a partir dos elementos da lista para manter apenas os elementos únicos e exibir esse conjunto.

# Escreva seu código aqui

lista=[]
for conj in range(10):
    perg = input("Digite um valor: ")
    lista.append(perg)
    
conjunto=set(lista)
print(conjunto)