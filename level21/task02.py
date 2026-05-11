# Abrindo o arquivo no modo de escrita e escrevendo a string "Hello, World!"
file = open('example.txt', 'w')
file.write("Hello, World!")
file.close()

# Abrindo o arquivo no modo de adição e adicionando a string "Appended text."
file = open('example.txt', 'a')
file.write("Appended text.")
file.close()