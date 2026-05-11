class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __str__(self):
        return f"Library with {len(self.books)} books: " + ", ".join(self.books)

    def __len__(self):
        return len(self.books)

# Criando um objeto da biblioteca
library = Library()

# Adicionando livros à biblioteca
library.add_book("Harry Potter and the Philosopher's Stone")
library.add_book("The Great Gatsby")
library.add_book("1984")

# Exibindo informações sobre a biblioteca com a lista de livros e a quantidade de livros
print(library)
print(f"Number of books in library: {len(library)}")