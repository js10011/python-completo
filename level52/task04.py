binary_str = input("Digite um número binário: ")
decimal_number = int(binary_str, 2)

# Calculando a quantidade de bytes
num_bytes = (decimal_number.bit_length() + 7) // 8

print(f"Representação decimal: {decimal_number}")
print(f"Quantidade de bytes: {num_bytes}")
print(f"Armazenamento na memória: {decimal_number.to_bytes(num_bytes, 'big')}")