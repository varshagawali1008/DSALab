def postfixToInfix (postfix):
    stack=[]
    i=0
    while i< len(postfix):
           if not isoperator(postfix[i]):
                 stack.append(postfix[i])
               
           else:
                o1 = stack.pop()
                o2 = stack.pop()
                str = o2 + postfix[i] + o1
                stack.append(str)
           i+=1
    return stack.pop()
def isoperator(c):
    if c=="*"or c=="+"or c=="-"or c=="/" or c=="^" :
        return True
    else:
        return False

str="ABC/-AK/L-*"
print(postfixToInfix (str))
