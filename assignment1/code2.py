'''

2.Given a dict of tickets("to":"from")

{"Chennai":"Banglore","Bombay":"Delhi","Goa":"Chennai","Delhi":"Goa"} find out the sequence of travel.

Expected Output : Bombay->Delhi, Delhi->Goa, Goa->Chennai, Chennai->Banglore

Function Name : travel_sequence Input : dict Output : dict

'''

d={"Chennai":"Banglore","Bombay":"Delhi","Goa":"Chennai","Delhi":"Goa"}
op = dict()

lst = d.keys()
start=sorted(list(lst))[0]

first = op.setdefault(start,d[start])
second = op.setdefault(first,d[first])
third = op.setdefault(second,d[second])
fourth = op.setdefault(third,d[third])
print("input:",d)
print("output sequence:",op)