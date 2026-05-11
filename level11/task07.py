# Criamos um dicionário com informações sobre o livro
book_info = {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "year": 1960
}

# Verificação da presença da chave "author" usando o operador in
if "author" in book_info:
    print("Chave 'author' encontrada")

# Verificação da presença da chave "publisher" usando o método get()
if book_info.get("publisher") is not None:
    print("Chave 'publisher' encontrada")
else:
    print("Chave 'publisher' não encontrada")

# Verificação da presença da chave "title" usando o método keys()
if "title" in book_info.keys():
    print("Chave 'title' encontrada")