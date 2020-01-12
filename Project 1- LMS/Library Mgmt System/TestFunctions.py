# -*- coding: utf-8 -*-
from Book import Book
from Catalog import Catalog
from User import Member, Librarian

# b1 = Book('Shoe Dog','Phil Knight', '2015',312)
# b1.addBookItem('123hg','H1B2','#1234')
# b1.addBookItem('124hg','H1B3','#4433')

# b1.printBook()

catalog = Catalog()

# b = catalog.addBook('Shoe Dog','Phil Knight', '2015',312)
# catalog.addBookItem(b, '123hg','H1B2',"#2222")
# catalog.addBookItem(b, '124hg','H1B4',"#6858")
# catalog.addBookItem(b, '125hg','H1B5',"#6833")

# b = catalog.addBook('Moonwalking with Einstien','J Foer', '2017',318)
# catalog.addBookItem(b, '463hg','K1B2',"#2343")

# b = catalog.addBook('The Harry Potter',"Jack daniel","2001",500)
# b = catalog.addBook('The Age of altron',"Jack daniel","2002",534)
# b = catalog.addBook('The Marvel king',"Jack daniel","2003",556)


# catalog.displayDifferentBooks()
# catalog.displayAllBookItems()
# print(catalog.searchByName("Shoe Dog"))


librarian = Librarian("Awantik","Bangalore",34,'asljlkj22','zeke101') 
print(librarian)




print("---------------------------------------------------")
print("From library class persepective")
print("---------------------------------------------------")

# l = catalog.searchByAuthor('Jack daniel')
# print(l)


# print(catalog.__dict__)



two_states = librarian.addBook(catalog,"2 states","Chetan Bhagat",'2010',340)
librarian.addBookItem(catalog,two_states, '554hg','S1B2',"#2287")
librarian.addBookItem(catalog,two_states, '555hg','S1B4',"#2284")
print(librarian.__dict__)
catalog.displayDifferentBooks()
catalog.displayAllBookItems()

shoe_dog = librarian.addBook(catalog,'Shoe Dog','Phil Knight', '2015',312)

librarian.addBookItem(catalog,shoe_dog, '123hg','H1B2',"#2222")
librarian.addBookItem(catalog,shoe_dog, '124hg','H1B4',"#6858")
librarian.addBookItem(catalog,shoe_dog, '125hg','H1B5',"#6833")

moon_walking = librarian.addBook(catalog,'Moonwalking with Einstien','J Foer', '2017',318)
librarian.addBookItem(catalog,moon_walking, '463hg','K1B2',"#2343")

harry_potter = librarian.addBook(catalog,'The Harry Potter',"Jack daniel","2001",500)
age_of_altron = librarian.addBook(catalog,'The Age of altron',"Jack daniel","2002",534)
marvel_king = librarian.addBook(catalog,'The Marvel king',"Jack daniel","2003",556)


# librarian.displayDifferentBooks(catalog)
# librarian.displayAllBookItems(catalog)
# librarian.removeBook(catalog,"2 states")
# librarian.displayDifferentBooks(catalog)
# librarian.displayAllBookItems(catalog)


# librarian.displayDifferentBooks(catalog)
# librarian.displayAllBookItems(catalog)
# librarian.removeBookItem(catalog,'2 states','#2287')
# librarian.displayDifferentBooks(catalog)
# librarian.displayAllBookItems(catalog)

print("##################")
print("user operations")
print("##################")

member = Member('sagar','jaipur',21,344564,33033)
print(member)



# member.searchCatalogByName(catalog,'2 states')

# member.searchCatalogByAuthor(catalog,'Chetan Bhagat')

# print(member.showInventory(catalog))

librarian.displayDifferentBooks(catalog)
librarian.displayAllBookItems(catalog)
rinfo1 = member.issueBook(catalog,'2 states','#2287')
rinfo2 = member.issueBook(catalog,'2 states','#2284')
librarian.displayDifferentBooks(catalog)
librarian.displayAllBookItems(catalog)


# print(rinfo1)


print(member.bookIssued)



# librarian.displayAllBookItems(catalog)
# librarian.displayDifferentBooks(catalog)

print("-----------------------------------------------------")
member.returnBook(catalog,'2 states',rinfo1,10,21)  #rinfo1 contains all info of issued book 
print("-----------------------------------------------------")


print("----after return things------")

librarian.displayAllBookItems(catalog)
librarian.displayDifferentBooks(catalog)









