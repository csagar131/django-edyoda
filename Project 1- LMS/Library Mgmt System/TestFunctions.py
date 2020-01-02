# -*- coding: utf-8 -*-
from Book import Book
from Catalog import Catalog
from User import Member, Librarian

# b1 = Book('Shoe Dog','Phil Knight', '2015',312)
# b1.addBookItem('123hg','H1B2','#1234')
# b1.addBookItem('124hg','H1B3','#4433')

# b1.printBook()

catalog = Catalog()

b = catalog.addBook('Shoe Dog','Phil Knight', '2015',312)
# catalog.addBookItem(b, '123hg','H1B2',"#2222")
# catalog.addBookItem(b, '124hg','H1B4',"#6858")
# catalog.addBookItem(b, '125hg','H1B5',"#6833")

b = catalog.addBook('Moonwalking with Einstien','J Foer', '2017',318)
#catalog.addBookItem(b, '463hg','K1B2',"#2343")

b = catalog.addBook('The Harry Potter',"Jack daniel","2001",500)
b = catalog.addBook('The Age of altron',"Jack daniel","2002",534)
b = catalog.addBook('The Marvel king',"Jack daniel","2003",556)


catalog.displayDifferentBooks()
#catalog.displayAllBookItems()

# m1 = Member("Vish","Bangalore",23,'asljlkj22','std1233')

librarian = Librarian("Awantik","Bangalore",34,'asljlkj22','zeke101') 
# print (m1)
# print (librarian)

#m1.issueBook

#print(catalog.searchByName("Shoe Dog"))
print("---------------------------------------------------")


# l = catalog.searchByAuthor('Jack daniel')
# print(l)

# c =  librarian.accesCatalog
# print(c.__dict__)
# print(catalog.__dict__)

#catalog.addBook("2 states","Chetan Bhagat",'2010',340)
librarian.addBook("2 states","Chetan Bhagat",'2010',340)

# print(librarian.__dict__)
# catalog.displayDifferentBooks()
librarian.displayDifferentBooks()



# print(catalog.accessCurrentCatalog())
# print(librarian.accessCurrentCatalog())