def check_empty(d):
    return len(d) == 0

# Criamos vários dicionários com diferentes quantidades de elementos
dict1 = {}
dict2 = {'a': 1, 'b': 2}
dict3 = {'x': 10}
dict4 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

dictionaries = [dict1, dict2, dict3, dict4]

# Exibimos a quantidade de elementos em cada dicionário e verificamos se estão vazios
for i, d in enumerate(dictionaries, 1):
    print(f"Dicionário {i}: {len(d)} elementos")
    if check_empty(d):
        print(f"Dicionário {i} está vazio")
    else:
        print(f"Dicionário {i} não está vazio")