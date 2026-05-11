# Criamos um dicionário com informações sobre o estudante
student_info = {
    'nome': 'Alice',
    'idade': 21,
    'universidade': 'Harvard'
}

# Iteramos sobre os pares chave-valor do dicionário usando a função enumerate
for index, (key, value) in enumerate(student_info.items()):
    print(f"Index: {index}, Key: {key}, Value: {value}")