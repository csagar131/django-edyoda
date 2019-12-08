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

            





    




