# Gerador de quadrados

# Escreva um programa que crie um conjunto de quadrados de números de 1 a 10 usando um gerador de conjuntos.
# O programa deve exibir o conjunto obtido.

# Escreva seu código aqui

# Criação do conjunto de 10 números aleatórios no intervalo de 1 a 100

'''for i in range(1,11):
    i **=2
    x = {i}
    print(x)'''
    
squares = {i*i for i in range(1, 11)}
print(squares)