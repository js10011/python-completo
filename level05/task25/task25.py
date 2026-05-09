# Adição de elemento

# Escreva um programa que crie uma tupla com 5 elementos solicitados do usuário.
# Em seguida, o programa deve solicitar ao usuário um novo elemento e adicioná-lo ao final da tupla, criando uma nova tupla.
# O programa deve imprimir a tupla atualizada.

# Escreva seu código aqui
# 1. Criando uma lista vazia para armazenar os inputs iniciais
elementos = []

print("Digite 5 elementos para a sua tupla:")
for i in range(5):
    item = input(f"Elemento {i+1}: ")
    elementos.append(item)

# 2. Convertendo a lista em uma tupla
tupla_original = tuple(elementos)

# 3. Solicitando o novo elemento
novo_elemento = input("Digite um novo elemento para adicionar: ")

# 4. "Adicionando" o elemento criando uma nova tupla
# Nota: O novo elemento precisa estar entre parênteses e com uma vírgula 
# para ser reconhecido como uma tupla de um único item (singleton).
tupla_atualizada = tupla_original + (novo_elemento,)

# 5. Imprimindo o resultado
print("\nTupla original:", tupla_original)
print("Tupla atualizada:", tupla_atualizada)