# -*- coding: utf-8 -*-
class BookItem:
    def __init__(self,book,isbn,rack,barcodeNo):
        self.book = book
        self.isbn = isbn
        self.rack = rack
        self.barcodeNo = barcodeNo

    def __repr__(self):
        return self.book.name + ' ' + self.isbn
        
