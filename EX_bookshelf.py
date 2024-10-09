class Book:

    book_count = 0     #counter that keeps track of the number of books

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author    #both name and surname
        self.isbn = isbn        #International Standard Book Number, search online for more information
        Book.book_count += 1

    def print_book_info(self):
        print (f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}")

    @staticmethod
    def print_book_count():
        print (f"Total number of books: {Book.book_count}")

book1 = Book("The Alchemist", "Paulo Coelho", "978-0062315007")
book2 = Book("The Kite Runner", "Khaled Hosseini", "978-1594631931")
book3 = Book("The Da Vinci Code", "Dan Brown", "978-0307474278")

book1.print_book_info()
book2.print_book_info()
book3.print_book_info()

Book.print_book_count()