# -*- coding: utf-8 -*-
from BookItem import BookItem

class Book:
    def __init__(self,name,author,publish_date,pages):
        self.name = name
        self.author = author
        self.publish_date = publish_date
        self.pages = pages
        self.total_count = 0 # total count of all the bookItem in inventory
        self.book_item = []  #bookItems of perticular book
        
    def __repr__(self):
        return self.name
    
    def addBookItem(self,isbn,rack,barcode):
        b = BookItem(self,isbn,rack,barcode)
        self.book_item.append(b)
        self.total_count +=1
        
    def printBook(self):
        print(self.name,self.author)
        for book_item in self.book_item:
            print(book_item.isbn,book_item.barcodeNo,book_item.book.name)
        print("------------------------------------------------")
