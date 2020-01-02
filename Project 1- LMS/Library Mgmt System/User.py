# -*- coding: utf-8 -*-
from Catalog import Catalog

class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id
        

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
        
    def __repr__(self):
        return self.name + self.location + self.emp_id
    
    # to access the catalog features by the Librarian/Admin
    def accessCurrentCatalog(self):   
        catalog = Catalog().accessCurrentCatalog()
        return catalog

    # to add the book in the catalog by the librarian
    def addBook(self,name,author,publish_date,pages):
        catalog = self.accessCurrentCatalog()
        catalog.addBook(name,author,publish_date,pages)


    def displayDifferentBooks(self):
        catalog = self.accessCurrentCatalog()
        catalog.displayDifferentBooks()

    # to add the bookItem of perticular book 
    def addBookItem(self,isbn,rack,barcode):
        pass
    
    def removeBook(self,name):
        pass
    
    
        