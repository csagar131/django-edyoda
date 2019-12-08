'''
1.In the pre-smartphone era,each number key is assigned a subset of the alphabet {a,b,…,z}.

- 2 is assigned {a,b,c}, 
- 3 is assigned {d,e,f} 
- 4 is assigned {g,h,i} 
- 5 is assigned {j,k,l}
- 6 is assigned {m,n,o} 
- 7 is assigned {p,q,r,s}
- 8 is assigned {t,u,v} 
- 9 is assigned {w,x,y,z}

Write a function numbers_to_chars() to find the characters generated using key 9999335533. Output should be "zeke"

Function Name : numbers_to_chars() Input : Integer number sequence Output : Str
'''


d={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
op = []

def numbers_to_chars():
    s =''
    n = int(input("enter your number:"))
    lst = list(str(n))
    temp = []
    for i in range(len(lst)):
        count = 1
        if lst[i] in temp:
            continue
        temp.append(lst[i])
        if len(temp) > 1:
            temp.pop(0)
        for j in range(i,len(lst)-1):
            if lst[i] == lst[j+1]:
                count+=1
            else:
                break
        op.append(d[lst[i]][count-1])
    s=s.join(op)
    print(s)

numbers_to_chars()
