def custom_hash(d):
    hash_value = 0
    for key, value in d.items():
        hash_value += hash(key)
        hash_value += hash(value)
    return hash_value % 10000

# Exemplo de uso
sample_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
print(custom_hash(sample_dict))