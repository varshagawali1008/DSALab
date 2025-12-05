def prec(c):
    if c == '^':
        return 3
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1

def infixTOpostfix(s):
    st = []
    result = ""
    
    for c in s:
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
    
    return result

# Example
exp = "a+b*c-d"
print("Postfix Expression:", infixTOpostfix(exp))
