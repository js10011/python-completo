# Quinto elemento.

# Escreva um programa que crie uma lista de 5 elementos solicitados ao usuário.
# O programa deve imprimir a lista, depois solicitar ao usuário o índice de um elemento e exibir o valor do elemento nesse índice.

# Escreva seu código aqui
itens= []
for x in range(5):
    perg = input("Adicione algo à lista: ")
    itens.append(perg)
print(itens)

index = int(input("Qual elemento vc deseja saber o indice? "))

print(itens[index])