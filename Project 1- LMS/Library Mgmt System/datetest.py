from datetime import date,datetime,timedelta
print(dir(date))



d1 = date.today()

# d2 =  date(2020,2,11)

# da = d2 - d1
# print(type(da))

# print(d1)
# d1.day+= 5
# print(d1)
# #print(type(d3))


currenttime  = datetime.now()
returntime   = currenttime + timedelta(days=20)

info = returntime - currenttime
info = int(str(info).split(" ")[0])
print(currenttime)
print(returntime)
print(info)

# k =  str(datetime.now() + timedelta(days)).split(" ")[0]
# print(k)
# print(type(k))


# check if inventory becomes empty
# if self.catalog.inventory[name] == 0:
#     self.catalog.different_book_count-= 1 # reduce the book count 
#     self.catalog.inventory.pop(name) 
#     self.catalog.books.remove(book)