'''
7.Write a program to check the strength of a supplied password
The length of the password must be at least 8 characters in length The password must contain at least 1 capital letter
The password must contain at least 1 digit The password must contain at least 1 special character and allowed special
characters are (!,@,#,$,&)
We need to provide feedback to the user about the strength of their password
Provide the user with a list of reasons why their password is 'weak'
Function Name : check_password_strength Input : str Output : tuple (str,list) eg ("Weak",["The password must contain
at least 1 capital letter"])

'''

def check_password_strength(p):
    ans = ['Weak']
    lst = p
    dg = []
    if len(lst) < 8:
        ans.append(['the password must be at least 8 characters in length'])
        reason = tuple(ans)
        print(reason)
        return
    if len(lst) >= 8:
        for i in ['!','@','#','$','&']:
            if i in lst:
                if len(ans) > 1:
                    ans =  ans[:1]
                    break
            else:    
                ans.append(['The password must contain at least 1 special character'])
                if len(ans) > 1:
                    ans =  ans[:2]

        if lst.islower():
            ans.append(['The password must contain at least 1 capital letter'])
        

        for i in lst:
            try:
                if int(i):
                    if dg:
                        dg = []
                        break
            except:
                dg.append(['The password must contain at least 1 digit'])
                continue
        if dg:
            ans.append(dg[0])
        
    if len(ans) > 1:
        print(tuple(ans))
    else:
        print("Password is Strong")
           


p=input("Enter password:")
check_password_strength(p)
