# Criando um dicionário com informações sobre um livro
book_info = {
    "title": "Crime e Castigo",
    "author": "Fiódor Dostoiévski",
    "year": 1866
}

# Exibindo todas as chaves do dicionário usando o método keys()
keys = book_info.keys()
print(keys)

# Iterando por todas as chaves e exibindo-as na tela
for key in keys:
    print(key)