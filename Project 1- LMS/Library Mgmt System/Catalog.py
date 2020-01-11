# -*- coding: utf-8 -*-
from Book import Book
#First Book is file & second is Class

#Catalog class maintains all the information about the book and bookItems of Book
class Catalog:
    
    def __init__(self):
        self.different_book_count = 0
        self.books = []
        self.inventory = dict() 
        #inventory to store the complete details of book and its bookItems 
        

    #Only available to admin
    def addBook(self,name,author,publish_date,pages):
        b = Book(name,author,publish_date,pages)
        self.different_book_count += 1
        self.books.append(b)
        self.inventory.setdefault(b.name,0)  #adding book to inventory initially zero
        return b
    
    #Only available to admin
    def addBookItem(self,book,isbn,rack,barcodeNo):
        book.addBookItem(isbn, rack, barcodeNo)
        self.inventory[book.name]+= 1  #increase bookItem count when bookItem added
        
    def searchByName(self,name):
        for book in self.books:  
            if name == book.name:  #return true if book requested is available
                return book
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
        print('Different Book Count',self.different_book_count)
        print(self.inventory)

    #display the bookItem details of book
    def displayAllBookItems(self):
        #self.displayDifferentBooks()
        c = 0
        for book in self.books:
            c += book.total_count
            book.printBook()
        print ('Total BookItem Count',c)
