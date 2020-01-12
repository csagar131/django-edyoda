# -*- coding: utf-8 -*-

from Catalog import Catalog
from datetime import date,datetime,timedelta

class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id
        #self.catalog = Catalog()  #creating  a catalog object
        

class Member(User):
    def __init__(self,name, location, age, aadhar_id,student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        self.issueLimit = 3
        self.bookIssued = []
        
    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + str(self.student_id)
    

    #assume name is unique
    def issueBook(self,catalog,name,barcode,days=10):
        transaction = []  #store the current transaction details
        self.days = days
        book = catalog.searchByName(name) # search in the books objects  # if requested book present
        try:
            #check count of booItem in inventory and   check the member issue limit
            if catalog.inventory.get(name) > 0 and self.issueLimit > 0:
                for bookitem in book.book_item: # search for bookItem of requested barcode
                    if bookitem.barcodeNo == barcode:  # if requested barcode present
                        book.book_item.remove(bookitem) #remove bookItem of that barcode
                        book.total_count-= 1  #decrease total count of bookItems
                        catalog.inventory[name]-= 1  #decrease the count of that book in inventory
                        self.issueLimit-= 1  # reduce the book issue limit of member
                        print('you can issue {} more books'.format(self.issueLimit))
                        returndays = self.returnDays(days) #will return total days from issue date to return date
                        transaction.extend([(datetime.now()),book.name,bookitem.isbn,bookitem.rack,barcode,returndays])  #make a transaction
                        self.bookIssued.append(transaction) #associate the details of transaction with member
                        return transaction             
        except:
            print("bookItem of book {} not present".format(book.name))
            return
        
        print("book of name {} not present in inventory".format(name))
            

    # issue book return inforamation
    def returnDays(self,days):
        currenttime  = datetime.now()
        returntime   = currenttime + timedelta(days)  
        info = returntime - currenttime
        info = int(str(info).split(" ")[0])
        return info #total days from issue date to return date


    #show the whole collection of book and bookItem
    def showInventory(self,catalog):
        return catalog.inventory

    
    #assume name is unique
    def returnBook(self,catalog,name,rinfo,issuedays,returndays):
        #print(name,issuedays,returndays)
        fineAmt = 0
        bkitem = [bitem for bitem in self.bookIssued if rinfo[-2] in bitem]
        if bkitem:  #check the book is that whick is issued
            #[(datetime.now()),book.name,bookitem.isbn,bookitem.rack,barcode,returndays]
            book = catalog.searchByName(name)
            #book = [bk for bk in catalog.books if bk.name == rinfo[1]][0]
            catalog.addBookItem(book,rinfo[2],rinfo[3],rinfo[4])
            catalog.inventory[book.name]+= 1  #increase the count of that book in inventory
            self.issueLimit+= 1  # update the book issue limit of member
            self.bookIssued.remove(rinfo)  # remove that transaction from member account
            fineAmt = self.payFine(returndays-issuedays)
            print("Return successful")
            print("please pay the fine of {} to librarian".format(fineAmt))
        else:
            print("please bring associated with this library")
        

    #for paying fine
    def payFine(self,noOfDays):
        fineAmt = 0
        if noOfDays <= 10:  # now we are checking only for 10 days
            return 0
        else:
            fineAmt = (noOfDays-10) * 2 # if greater than 10 days count from 11th day
            return fineAmt

    
    #for searching all the available book present in catalog by name
    def searchCatalogByName(self,catalog,name):
        result = catalog.searchByName(name) #if book of required name found
        if result:
            print("book of name {} is present".format(name))
            return True
        else:
            print("book of name {} is not present".format(name))
            return False
        

    #for searching all the available book present in catalog by author
    def searchCatalogByAuthor(self,catalog,author):
        result = catalog.searchByAuthor(author)
        if result:  #if book of required author found
            print("all the books by author {} is/are {}".format(author,result))
        else:
            print("book of author {} not present now".format(author))  
        
        
class Librarian(User):
    
    def __init__(self,name, location, age, aadhar_id,emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id
        
    #string representation of the object
    def __repr__(self):
        return self.name +' '+ self.location +' '+ self.emp_id
    

    # to add the book in the catalog by the librarian
    def addBook(self,catalog,name,author,publish_date,pages):
        #only librarian can add the book to catalog
        # returning the book object and storing in self.book for later use
        self.book = catalog.addBook(name,author,publish_date,pages)  # returning the book object
        return self.book         # returning book object
                                                                          

    # to display No. of different Books
    def displayDifferentBooks(self,catalog):
        catalog.displayDifferentBooks()


    # to add the bookItem of perticular book 
    def addBookItem(self,catalog,book,isbn,rack,barcode):
        #we are calling the already defined function of catalog class
        #only librarian can add the bookItem to catalog
        catalog.addBookItem(self.book,isbn,rack,barcode)  
    

    #display all the book item with different book
    def displayAllBookItems(self,catalog):
        catalog.displayAllBookItems()


    #for removing the book so its bookItem will also deleted
    def removeBook(self,catalog,name):
        self.bookItemslen = 0
        bookobj = catalog.searchByName(name)
        catalog.books.remove(bookobj)  #remove book object from list of books
        catalog.different_book_count-=1  # reduce the different book count
        bookobj.book_item.clear() #clearing the bookItem list of perticular list
        self.bookItemslen = len(bookobj.book_item) #determining total bookitems of book
        bookobj.total_count-=self.bookItemslen #reducing total book count
        catalog.inventory.pop(bookobj.name)
    

    #to remove the bookItem based on the barcodeNo from inventory
    def removeBookItem(self,catalog,name,barcodeNo):
        books = catalog.searchByName(name)
        for bookItem in books.book_item:
            if bookItem.barcodeNo == barcodeNo:
                books.book_item.remove(bookItem)
                catalog.inventory[books.name]-= 1
                books.total_count-= 1

                        
                
           
        
        

    
    
        