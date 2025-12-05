class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinearQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new = Node(data)
        if self.rear is None:
            self.front = self.rear = new
        else:
            self.rear.next = new
            self.rear = new

    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
            return
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.data

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# ---- Driver Code ----
q = LinearQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

print("Dequeued:", q.dequeue())
q.display()
