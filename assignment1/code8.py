'''
Check if given sentence is syntactically correct or not
A simple sentence if syntactically correct if it fulfills given rules. The following are given rules.

Sentence must start with a Uppercase character (e.g. Noun/ I/ We/ He etc.)
There must be spaces between words.
Then the sentence must end with a full stop(.).
Two continuous spaces are not allowed.
Two continuous uppercase characters are not allowed.
However the sentence can end after an uppercase character.
Function Name : check_sentence Input : str 
Output : tuple (True/False,list) eg (False,["There must be spaces between words."])
'''

def check_sentance(s):
    correct = True
    ans = []
    
    if not s[0].isupper():
        correct = False
        ans.append(['Sentence must start with a Uppercase character.'])
    
    if not ' ' in s:
        correct = False
        ans.append(['There must be spaces between words.'])
    
    if '  ' in s:
        correct = False
        ans.append(['Two continuous spaces are not allowed.'])
    
    if not s.endswith('.'):
        correct = False
        ans.append(['the sentence must end with a full stop(.).'])
        if s[len(s)-1].isupper():
            correct = True
            ans.pop()
    
    for i in range(len(s)-1):
        if s[i].isupper() and s[i+1].isupper():
            correct = False
            ans.append(['Two continuous uppercase characters are not allowed.'])
            break
    if ans:
        lst = [correct,ans]    
        return tuple(lst)
    else:
        return "Sentance is correct"


#sentance = input("Enter sentance:")
#ans = check_sentance(sentance)
#print(ans)



