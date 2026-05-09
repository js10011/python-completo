# Tupla do Usuário

# Escreva um programa que cria uma tupla a partir de um número arbitrário de elementos fornecidos pelo usuário.
# Em seguida, o programa deve exibir o último elemento da tupla.
# Se a tupla estiver vazia, o programa deve exibir uma mensagem sobre isso.

# Escreva seu código aqui
num = input("Digite os valores: ")
valores = num.split()
tupla = tuple(valores)

if not tupla :
    print("vazia")
    
else:
    print(tupla[-1])