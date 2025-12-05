class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.front = None

    def enqueue(self, data, priority):
        new_node = Node(data, priority)
        if self.front is None or priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
        else:
            temp = self.front
            while temp.next and temp.next.priority <= priority:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

    def dequeue(self):
        if self.front is None:
            return None
        temp = self.front
        self.front = self.front.next
        return temp.data

    def display(self):
        temp = self.front
        while temp:
            print(f"{temp.data}({temp.priority})", end=" ")
            temp = temp.next
        print()

pq = PriorityQueue()
pq.enqueue("A", 3)
pq.enqueue("B", 1)
pq.enqueue("C", 2)
pq.enqueue("D", 5)

print("Priority Queue:")
pq.display()

print("Dequeued:", pq.dequeue())
print("After Dequeue:")
pq.display()
