class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.rear = new_node
            self.rear.next = self.rear
        else:
            new_node.next = self.rear.next
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.rear is None:
            return None
        temp = self.rear.next
        if self.rear.next == self.rear:
            self.rear = None
        else:
            self.rear.next = temp.next
        return temp.data

    def display(self):
        if self.rear is None:
            print("Queue is empty")
            return
        temp = self.rear.next
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.rear.next:
                break
        print()

cq = CircularQueue()
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)

print("Circular Queue:")
cq.display()

print("Dequeued:", cq.dequeue())
print("After Dequeue:")
cq.display()
