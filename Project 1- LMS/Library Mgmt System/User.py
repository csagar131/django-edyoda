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
        
    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id
    
    #assume name is unique
    def issueBook(self,name,days=10):
        pass
    
    #assume name is unique
    def returnBook(self,name):
        pass

    #for paying fine
    def payFine(self):
        pass
    
    #for searching all the available book present in catalog
    def searchCatalog(self):
        pass
        
        
        
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
                                                                          

    # to display No. of different Books
    def displayDifferentBooks(self):
        self.catalog.displayDifferentBooks()

    # to add the bookItem of perticular book 
    def addBookItem(self,book,isbn,rack,barcode):
        #we are calling the already defined function of catalog class
        #only librarian can add the bookItem to catalog
        self.catalog.addBookItem(self.book,isbn,rack,barcode)  
    
    def removeBook(self,name):
        pass
    
    
        