
class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        
#insert node at beginning
        
    def AddAtBeginning(self,newdata):
       NewNode=Node(newdata)
       NewNode.next=self.head
       self.head=NewNode

#insert node at end
    def AddAtEnd(self,newdata):
        NewNode=Node(newdata)
        NewNode.next=self.None
        self.None=NewNode
       
#print linked list
       
    def ListPrint(self):
        temp=self.head
        print("linked list:")
        while temp is not None:
            print(temp.data,"->")
            temp=temp.next
        print("None")
ll=LinkedList()
ll.AddAtBeginning(20)
ll.AddAtBeginning(10)
ll.ListPrint()
ll.AddAtBeginning(50)
ll.ListPrint()
            
    
