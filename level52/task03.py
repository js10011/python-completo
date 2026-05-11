number = int(input("Digite um número inteiro: "))
binary_representation = bin(number)[2:]
byte_count = (number.bit_length() + 7) // 8
print(f"Representação binária: {binary_representation}")
print(f"Quantidade de bytes: {byte_count}")