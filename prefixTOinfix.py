def prefixToInfix (prefix):
    stack=[]
    i=len(prefix)-1
    while i>=0:
           if not isoperator(prefix[i]):
                stack.append(prefix[i])
                i-=1
           else:
                 str=stack.pop()+prefix[i]+stack.pop()
                 stack.append(str)
                 i-=1
    return stack.pop()
def isoperator(c):
    if c=="*"or c=="+"or c=="-"or c=="/" or c=="^" :
        return True
    else:
        return False

str="*-A/BC-/AKL"
print(prefixToInfix (str))
