'''
10.Given a list of N integers. The task is to eliminate the minimum number of elements such that
in the resulting list the sum of any two adjacent values is even.
Numbers = [1, 3, 5, 4, 2] Output = [1, 3, 5] Total elements removed 2 Elements to be removed [4,2]

Function Name : adj_sum_even() Input : list Output : tuple(int,list)

'''
temp = []
count = 0
def adj_sum_even(lst):
    try:
        for i in range(len(lst)-1):
            if (lst[i] + lst[i+1]) % 2 == 0:
                continue
            else:
                if lst[i] % 2 == 0:
                    temp.append(lst[i])
                    lst.remove(lst[i])
                    adj_sum_even(lst)
                else:
                    temp.append(lst[i+1])
                    lst.remove(lst[i+1])
                    adj_sum_even(lst)
    except:
        return lst



print("Enter list of elements")
lst = input().split(' ')
for i in range(len(lst)):
    lst[i] = int(lst[i])
l=adj_sum_even(lst)
print("list after removing elements",l)
print(tuple(temp),str(len(temp))+" elements are removed")