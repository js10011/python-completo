# Solicitando 5 elementos do usuário e criando uma tupla
elements = tuple(input(f"Digite o elemento {i+1}: ") for i in range(5))

# Solicitando o índice do elemento
index = int(input("Digite o índice do elemento: "))

# Verificando se o índice está dentro dos limites da tupla e exibindo a mensagem correspondente
if 0 <= index < len(elements):
    print(f"Elemento no índice {index}: {elements[index]}")
else:
    print("Índice está fora dos limites da tupla")