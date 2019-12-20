'''
4.How do you check if a given String contains valid parentheses? Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
write a program in python to check if the input string is valid. The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
Function Name : check_parentheses Input : str Output : True/False
'''


def check_parentheses(s):
    ans = False
    stack = []
    lst = [char for char in s]

    for i in range(len(lst)):
        if lst[i] == '(':
            stack.append(lst[i])
        if lst[i] == '{':
            stack.append(lst[i])
        if lst[i] == '[':
            stack.append(lst[i])

        
        if stack[len(stack)-1] == '(' and lst[i] == ')':
            stack.pop()
        elif stack[len(stack)-1] == '[' and lst[i] == ']':
            stack.pop()
        elif stack[len(stack)-1] == '{' and lst[i] == '}':
            stack.pop()
        else:
            continue

    if not stack:
        ans = True
            
    return ans


#k = input("Enter string:")
#ans=check_parentheses(k)
#print(ans)