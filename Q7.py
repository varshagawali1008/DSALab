class Stack:
    def __init__(self):          # should be __init__ (double underscores)
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty. Cannot pop.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty. Cannot peek.")
            return None

    def size(self):
        return len(self.stack)

# Example usage
st = Stack()
st.push("1")
st.push("2")
st.push("3")
print("Stack is:", st.stack)
print("Pop:", st.pop())
print("Peek:", st.peek())
print("Size:", st.size())
