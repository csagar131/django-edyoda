'''
3.Given a dictionary that associates the names of states with a list of the names of cities that appear in it,write a program that creates a new dictionary that associates the name of a city with the list of states that it appears in.
As an example, if the first dictionary is
'''


# input
states = {'New Hampshire':['Concord', 'Hanover'],'Massachusetts':['Boston', 'Concord', 'Springfield'],
'Illinois':['Chicago', 'Springfield', 'Peoria']}

#output
'''
cities = {'Hanover': ['New Hampshire'],'Chicago': ['Illinois'],'Boston': ['Massachusetts'],
'Peoria': ['Illinois'],'Concord': ['New Hampshire','Massachusetts'],'Springfield': ['Massachusetts', 'Illinois'] }
'''

cities = dict()
clist = set()
for i in states.values():
    for j in i:
        clist.add(j)

clist = list(clist)

for city in clist:
    temp = []
    for key,value in states.items():
        if city in value:
            temp.append(key)
    cities[city] = temp
print(cities)

            





    




