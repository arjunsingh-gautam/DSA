# Insertion in a Singly Linked List at the beginning of the list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SingleLinkedList:
    def __init__(self):
        self.head=None

    # Insertion at beginning of the list
    def insert_beg(self,data):
        # New Node creationg
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        
        current=self.head
        new_node.next=current
        self.head=new_node

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
print("Length of list{}".format(l1.len))
l1.display()
l1.insert_beg(20)
print("Length of list{}".format(l1.len))
l1.display()
l1.insert_beg(30)
print("Length of list{}".format(l1.len))
l1.display()
l1.insert_beg(40)
print("Length of list{}".format(l1.len))
l1.display()