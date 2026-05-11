import pickle

# Exemplo de dicionário para serialização
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'Wonderland'
}

# Serialização do dicionário para string
serialized_data = pickle.dumps(data)

# Desserialização do dicionário da string
deserialized_data = pickle.loads(serialized_data)

# Imprime o resultado para verificação
print("Serialized data:", serialized_data)
print("Deserialized data:", deserialized_data)