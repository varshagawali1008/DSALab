# Function to check precedence
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

# Function to check if character is operand
def isOperand(c):
    return c.isalpha() or c.isdigit()

# Reverse the infix expression
def infix_to_prefix(infix):
    infix = infix[::-1]                     # reverse expression
    stack = []
    result = ""

    # replace ( with ) and vice-versa
    infix = list(infix)
    for i in range(len(infix)):
        if infix[i] == '(':
            infix[i] = ')'
        elif infix[i] == ')':
            infix[i] = '('
    infix = "".join(infix)

    for c in infix:
        if isOperand(c):
            result += c
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        else:
            while stack and precedence(c) <= precedence(stack[-1]):
                result += stack.pop()
            stack.append(c)

    while stack:
        result += stack.pop()

    return result[::-1]      # final reverse for prefix


# ---- Driver code ----
exp = "A+B*C"
print("Prefix Expression:", infix_to_prefix(exp))
