'''
9.Given an array arr[] of integers and an integer K, the task is to find the greatest contiguous sub-array of size K.
Sub-array X is said to be greater than sub-array Y if the first non-matching element in both the sub-arrays has a greater
value in X than in Y.
For example : Input: arr[] = {1, 4, 3, 2, 5}, K = 4 Output: 4 3 2 5 Two subarrays are {1, 4, 3, 2} and {4, 3, 2, 5}. First non-matching element from array1 and array 2 : 1 and 4 as 4 is greater Hence, the greater one is {4, 3, 2, 5}
Function Name : greatest_sub_array() Input : list Output : list

'''

def greatest_sub_array(lst,k):
    mx = lst[0]
    arr = []
    for i in range(0,len(lst)):
        count = 0
        p = i
        for j in range(0,k):
            if count != k:
                arr.append(lst[p])
                p+=1
        
        if i == len(lst) - k:
            return arr

        if mx < lst[i+1]:
            mx = lst[i+1]
            arr = []
        else:
            if len(arr) >= k:
                arr = []
            continue  
        
    
#print("Enter array")
#lst = input().split()
#lst = [int(i) for i in lst]
#k = int(input("Enter integer k:"))

#anslst=greatest_sub_array(lst,k)
#print(anslst)
