# -*- coding: utf-8 -*-
from Book import Book
from Catalog import Catalog
from User import Member, Librarian

b1 = Book('Shoe Dog','Phil Knight', '2015',312)
b1.addBookItem('123hg','H1B2','#1234')
b1.addBookItem('124hg','H1B3','#4433')

b1.printBook()

catalog = Catalog()

b = catalog.addBook('Shoe Dog','Phil Knight', '2015',312)
catalog.addBookItem(b, '123hg','H1B2',"#2222")
catalog.addBookItem(b, '124hg','H1B4',"#6858")
catalog.addBookItem(b, '125hg','H1B5',"#6833")

b = catalog.addBook('Moonwalking with Einstien','J Foer', '2017',318)
catalog.addBookItem(b, '463hg','K1B2',"#2343")

catalog.displayAllBooks()

# m1 = Member("Vish","Bangalore",23,'asljlkj22','std1233')

# librarian = Librarian("Awantik","Bangalore",34,'asljlkj22','zeke101') 
# print (m1)
# print (librarian)

#m1.issueBook

#print(catalog.searchByName("Shoe Dog"))
print("---------------------------------------------------")