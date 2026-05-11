# Criamos um dicionário com informações sobre um livro
book = {
    "título": "Guerra e Paz",
    "autor": "Liev Tolstói",
    "ano de publicação": 1869
}

# Alteramos o valor da chave "ano de publicação"
book["ano de publicação"] = 1873
print("Após a alteração do ano de publicação:", book)

# Usamos o método setdefault() para adicionar uma nova chave "editora"
book.setdefault("editora", "Editora AST")
print("Após a adição da editora:", book)

# Atualizamos os valores de vários elementos usando o método update()
book.update({
    "título": "Anna Kariênina",
    "autor": "Liev Tolstói",
    "ano de publicação": 1877
})
print("Após a atualização de vários elementos:", book)