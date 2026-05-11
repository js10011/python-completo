def custom_hash(s):
    hash_value = 0
    prime = 31
    for char in s:
        hash_value = (hash_value * prime + ord(char)) % 10000
    return hash_value

# Exemplo de uso
example_string = "Hello, World!"
print(custom_hash(example_string))