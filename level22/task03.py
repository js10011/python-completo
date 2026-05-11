import pickle

# Exemplo de lista para serialização
data = [1, 2, 3, 'a', 'b', 'c']

# Serialização da lista em um arquivo
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Desserialização da lista do arquivo
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

# Verificação do resultado
print(loaded_data)