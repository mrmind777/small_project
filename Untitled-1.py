class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books] 
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author            
Library = Library("New yourk public Library")

book1 = Book("Harry Potter...", "J.K. Rowling")  
book2 = Book("The Rings of Power", "J.R.R. Tolkien")  
book3 = Book("The Colour of Magic", "Terry Pratchett")

Library.add_book(book1)
Library.add_book(book2)
Library.add_book(book3)
print(Library.name)
for book in Library.list_books():
    print(book)