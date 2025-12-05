#stack implementation using linked list
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class Stack:
    def __init__(self):
        self.head=None
        self.size=0
    def push(self,value):
        new_node=Node(value)
        if self.head:
            new_node.next=self.head
        self.head=new_node    
        self.size+=1
    def pop(self):
         if self.isEmpty():
             return"Stack is empty"
         popped_node=self.head
         self.head=self.head.next
         return popped_node.value
    def peek(self):
         if self.isEmpty():
             return "stack is empty"
             return self.head.value                                                  
    def isEmpty(self):
        return self.size==0
    def stackSize(self):
        return self.size
    def display(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            current = self.head
            print("Stack elements (top → bottom): ", end="")
            while current:
                print(current.value, end=" ")
                current = current.next
            print()

s1=Stack()
s1.push("A")
s1.push("B")
s1.push("C")
s1.push("D")
s1.push("E")
print("Stack:",s1.display())
print("pop:",s1.pop())
print("peek:",s1.peek())
print("isEmpty:",s1.isEmpty())
print("Size:",s1.stackSize())
