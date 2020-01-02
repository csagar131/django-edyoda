# -*- coding: utf-8 -*-
from Book import Book
#First Book is file & second is Class

class Catalog:
    def __init__(self):
        self.different_book_count = 0
        self.books = []
        
    #Only available to admin
    def addBook(self,name,author,publish_date,pages):
        b = Book(name,author,publish_date,pages)
        self.different_book_count += 1
        self.books.append(b)
        return b
    
    #Only available to admin
    def addBookItem(self,book,isbn,rack,barcodeNo):
        book.addBookItem(isbn, rack, barcodeNo)
        
    def searchByName(self,name):
        for book in self.books:  
            if name == book.name:  #return true if book requested is available
                return True
        return False
    
    # will give list of all the books from particualr author
    def searchByAuthor(self,author):
        books_by_author = []
        for book in self.books:
            if author == book.author:      
                books_by_author.append(book.name)
        return books_by_author

    # to dislay total no of different book
    def displayDifferentBooks(self):
        print ('Different Book Count',self.different_book_count)

                 
    def displayAllBookItems(self):
        self.displayDifferentBooks()
        c = 0
        for book in self.books:
            c += book.total_count
            book.printBook()
        print ('Total Book Count',c)
