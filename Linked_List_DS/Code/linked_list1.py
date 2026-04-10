# In this module we will implement simple linked list
# Liked list traversal and insertion at end

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self,data):

        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        
        current=self.head
        while current.next: # Traverse to the last node
            current=current.next
        current.next=new_node

    def display(self):
        current=self.head
        while current:
            print(current.data,end='->')
            current=current.next
        print("None")

l1=LinkedList()
l1.insert(20)
l1.insert(30)
l1.insert(40)
l1.display()