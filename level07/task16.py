# Ordenação de strings por comprimento

# Escreva um programa que crie uma lista de 5 strings solicitadas ao usuário.
# Em seguida, o programa deve ordenar a lista pelo comprimento das strings e exibir a lista ordenada.

# Escreva seu código aqui
l=[]
for i in range(5):
    perg=input("Digite algo: ")
    l.append(perg)
    
    orden= sorted(l, key=len)
    print(orden)