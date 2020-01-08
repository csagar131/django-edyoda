# -*- coding: utf-8 -*-
from Book import Book
from Catalog import Catalog
from User import Member, Librarian

# # b1 = Book('Shoe Dog','Phil Knight', '2015',312)
# # b1.addBookItem('123hg','H1B2','#1234')
# # b1.addBookItem('124hg','H1B3','#4433')

# # b1.printBook()

# catalog = Catalog()

# b = catalog.addBook('Shoe Dog','Phil Knight', '2015',312)
# # catalog.addBookItem(b, '123hg','H1B2',"#2222")
# # catalog.addBookItem(b, '124hg','H1B4',"#6858")
# # catalog.addBookItem(b, '125hg','H1B5',"#6833")

# b = catalog.addBook('Moonwalking with Einstien','J Foer', '2017',318)
# #catalog.addBookItem(b, '463hg','K1B2',"#2343")

# b = catalog.addBook('The Harry Potter',"Jack daniel","2001",500)
# b = catalog.addBook('The Age of altron',"Jack daniel","2002",534)
# b = catalog.addBook('The Marvel king',"Jack daniel","2003",556)


# catalog.displayDifferentBooks()
#catalog.displayAllBookItems()

# m1 = Member("Vish","Bangalore",23,'asljlkj22','std1233')

librarian = Librarian("Awantik","Bangalore",34,'asljlkj22','zeke101') 
# print (m1)
# print (librarian)

#m1.issueBook

#print(catalog.searchByName("Shoe Dog"))
print("---------------------------------------------------")
print("From library class persepective")
print("---------------------------------------------------")

# l = catalog.searchByAuthor('Jack daniel')
# print(l)


# print(c.__dict__)
# print(catalog.__dict__)





#catalog.addBook("2 states","Chetan Bhagat",'2010',340)
two_states = librarian.addBook("2 states","Chetan Bhagat",'2010',340)
librarian.addBookItem(two_states, '554hg','S1B2',"#2287")
librarian.addBookItem(two_states, '555hg','S1B4',"#2284")
# print(librarian.__dict__)
# catalog.displayDifferentBooks()

shoe_dog = librarian.addBook('Shoe Dog','Phil Knight', '2015',312)

librarian.addBookItem(shoe_dog, '123hg','H1B2',"#2222")
librarian.addBookItem(shoe_dog, '124hg','H1B4',"#6858")
librarian.addBookItem(shoe_dog, '125hg','H1B5',"#6833")

moon_walking = librarian.addBook('Moonwalking with Einstien','J Foer', '2017',318)
librarian.addBookItem(moon_walking, '463hg','K1B2',"#2343")

harry_potter = librarian.addBook('The Harry Potter',"Jack daniel","2001",500)
age_of_altron = librarian.addBook('The Age of altron',"Jack daniel","2002",534)
marvel_king = librarian.addBook('The Marvel king',"Jack daniel","2003",556)


print("displaying different books")
librarian.displayDifferentBooks()
print("displaying the bookItems")
librarian.displayAllBookItems()


#librarian.removeBook("2 states")

# print("------------------------------@@")
# librarian.removeBookItem(two_states)
# print("------------------------------@@")

# librarian.displayDifferentBooks()
# librarian.displayAllBookItems()

print("-----------------")
print("member operations")
print("-----------------")

member = Member('sagar','jaipur',21,344564,33033)

member.__dict__['catalog'] =librarian.__dict__.get('catalog')


member.searchCatalogByName('2 states')

member.searchCatalogByAuthor('Chetan Bhagat')