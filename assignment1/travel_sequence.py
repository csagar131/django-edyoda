'''

2.Given a dict of tickets("to":"from")

{"Chennai":"Banglore","Bombay":"Delhi","Goa":"Chennai","Delhi":"Goa"} find out the sequence of travel.

Expected Output : Bombay->Delhi, Delhi->Goa, Goa->Chennai, Chennai->Banglore

Function Name : travel_sequence Input : dict Output : dict

'''

#d={"Chennai":"Banglore","Bombay":"Delhi","Goa":"Chennai","Delhi":"Goa"}

def travel_sequence(d):
    startlist = d.keys()
    destlist = d.values()
    op = dict()
    

    for city in startlist:
        if city not in destlist:
            start = city
    
    i = 0
    while i < len(startlist):
        op.setdefault(start,d[start])
        start = d[start]
        i+=1
    return op


# print("input:",d)
# print("output sequence:",travel_sequence(d))
