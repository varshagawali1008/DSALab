def evaluate_postfix(expression):
    stack = []

    for ch in expression:
        if ch.isdigit():               # operand
            stack.append(int(ch))
        else:                          # operator
            op2 = stack.pop()
            op1 = stack.pop()

            if ch == '+':
                stack.append(op1 + op2)
            elif ch == '-':
                stack.append(op1 - op2)
            elif ch == '*':
                stack.append(op1 * op2)
            elif ch == '/':
                stack.append(op1 / op2)

    return stack.pop()



exp = "231*+9-"
print("Result:", evaluate_postfix(exp))
