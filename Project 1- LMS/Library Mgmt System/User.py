# -*- coding: utf-8 -*-
from Catalog import Catalog

class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id
        self.catalog = Catalog()  #creating  a catalog object
        

class Member(User):
    def __init__(self,name, location, age, aadhar_id,student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        self.issueLimit = 3
        self.bookIssued = []
        
    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id
    


    #assume name is unique
    def issueBook(self,name,days=10):
        self.days = days
        for book in self.catalog.books:
            if name == book.name:
                if book.book_item > 0 and self.issueLimit > 0:
                    pass




        

    
    #assume name is unique
    def returnBook(self,name):
        pass

    #for paying fine
    def payFine(self):
        pass
    
    #for searching all the available book present in catalog by name
    def searchCatalogByName(self,name):
        result = self.catalog.searchByName(name)
        if result:
            print("book of name {} is present".format(name))
            return True
        else:
            print("book of name {} is not present".format(name))
            return False
        
    #for searching all the available book present in catalog by author
    def searchCatalogByAuthor(self,author):
        result = self.catalog.searchByAuthor(author)
        if result:
            print("all the books by author {} is/are {}".format(author,result))
        else:
            print("book of author {} not present now".format(author))



        
        
        
class Librarian(User):
    
    def __init__(self,name, location, age, aadhar_id,emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id
        
    #string representation of the object
    def __repr__(self):
        return self.name + self.location + self.emp_id
    
    

    # to add the book in the catalog by the librarian
    def addBook(self,name,author,publish_date,pages):
        #only librarian can add the book to catalog
        # returning the book object and storing in self.book for later use
        self.book = self.catalog.addBook(name,author,publish_date,pages)  # returning the book object
        return self.book         # returning book object
                                                                          

    # to display No. of different Books
    def displayDifferentBooks(self):
        self.catalog.displayDifferentBooks()

    # to add the bookItem of perticular book 
    def addBookItem(self,book,isbn,rack,barcode):
        #we are calling the already defined function of catalog class
        #only librarian can add the bookItem to catalog
        self.catalog.addBookItem(self.book,isbn,rack,barcode)  
    
    #display all the book item with different book
    def displayAllBookItems(self):
        self.catalog.displayAllBookItems()

    #for removing the book so its bookItem will also deleted
    def removeBook(self,name):
        for book in self.catalog.books:
            if book.name == name:
                self.catalog.books.remove(book)  #remove book object from list of books
                self.catalog.different_book_count-=1  # reduce the different book count
                self.removeBookItem(book)   #removing corresponding bookItem

    
    def removeBookItem(self,book):
        self.bookItemslen = 0   
        for bookobj in self.catalog.books:
            if bookobj == book:
                self.bookItemslen = len(book.book_item) #determining total bookitems of book
                book.book_item.clear() #clearing the bookItem list of perticular list
        book.total_count-=self.bookItemslen
        

    
    
        