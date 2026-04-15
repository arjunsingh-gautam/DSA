# In this module we will implement simple linked list
# Liked list traversal and insertion at end

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SingleLinkedList:
    def __init__(self):
        self.head=None

    # Used to insert a Node at the end of the current list
    def insert(self,data):
        # New Node creationg
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        
        current=self.head
        while current.next: # Traverse to the last node
            current=current.next
        current.next=new_node # Join new node to the lisst
        

    def display(self):
        current=self.head
        while current:
            print(current.data,end='->')
            current=current.next
        print("None")
    
    @property
    def len(self):
        length=0
        current=self.head
        while current:
            length+=1
            current=current.next
        return length

l1=SingleLinkedList()
l1.insert(20)
l1.insert(30)
l1.insert(40)
l1.display()
print("Length of list:{}".format(l1.len))