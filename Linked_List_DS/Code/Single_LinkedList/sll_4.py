# Insertion in the middle of the Linked List

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
    # Insertino at end of the list 
    def insert_end(self,data):
        # Creating a new node:
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        current=self.head 
        while current.next:
            current=current.next
        else: 
            current.next=new_node
    # Insertion in the middle of the list
    def insert_med(self,data,position):
        length=self.len
        if position<0 or position>length:
            print("Invalid Position")
        elif position==0:
            self.insert_beg(data)
        elif position==length:
            self.insert_end(data)
        else:
            new_node=Node(data)
            p=self.head
            q=None
            for _ in range(position):
                q=p
                p=p.next
            q.next=new_node
            new_node.next=p
     

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
print("Length of list:{}".format(l1.len))
l1.display()
l1.insert_end(20)
print("Length of list:{}".format(l1.len))
l1.display()
l1.insert_end(30)
print("Length of list:{}".format(l1.len))
l1.display()
l1.insert_end(40)
print("Length of list:{}".format(l1.len))
l1.display()
l1.insert_med(50,1)
print("Length of list:{}".format(l1.len))
l1.display()
