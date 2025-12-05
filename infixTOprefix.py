def prec(c):
    if c == '^':
        return 3
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1

def infixTOprefix(exp):
    st = []
    result = ""
    s=exp[::-1]
    
    for i in range (len(s)):
        c=s[i]
        # If operand, add to output
        if (c.isalpha() or c.isdigit()):
            result += c
        
        # If '(', push to stack
        elif c == '(':
            st.append(c)
        
        # If ')', pop until '('
        elif c == ')':
            while st and st[-1] != '(':
                result += st.pop()
            st.pop()  # remove '('
        
        # Operator encountered
        else:
            while st and prec(c) <= prec(st[-1]):
                result += st.pop()
            st.append(c)
    
    # Pop all remaining operators
    while st:
        result += st.pop()
        result=result[::-1]
    
    return result

# Example
exp = "a+b*c-d"
print("Prefix Expression:", infixTOprefix(exp))
