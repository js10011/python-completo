class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def display_books(self):
        for book in self.books:
            print(book)

# Criação de um objeto da classe Library
library = Library()

# Adição de alguns livros
library.add_book("War and Peace")
library.add_book("1984")
library.add_book("The Great Gatsby")

# Exibição da lista de todos os livros
library.display_books()