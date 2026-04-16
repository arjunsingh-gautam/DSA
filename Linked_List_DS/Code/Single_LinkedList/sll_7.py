# Deletion from end of the list

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
        if position<0 or position>=length:
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
     
    # Display the list by traversing
    def display(self):
        current=self.head
        while current:
            print(current.data,end='->')
            current=current.next
        print("None")
   
    # return lenght of the list 
    @property
    def len(self):
        length=0
        current=self.head
        while current:
            length+=1
            current=current.next
        return length
    
    # Search for the node containing given data
    def search(self,value):
        if not self.head:
            print("List is Empty!")
            return
        current=self.head
        position=0
        while current:
            if current.data==value:
                print(f"{value} found at index-{position}")
                return
            position+=1
            current=current.next
        
        print(f"{value} not present in list")
        
    # Deletes node from beginning
    def del_beg(self):
        if not self.head:
            print("List is empty")
            return
        else:
            current=self.head
            self.head=current.next
            del current
    
    # Deletes node from the end of the list
    def del_end(self):
        if not self.head:
            print("List is empty")
            return
        else:
            p=self.head
            q=None
            while p.next:
                q=p
                p=p.next
            if p==self.head:
                self.head=None
                del p
            else:
                del p
                q.next=None
    
    # Deletion in middle of the list:
    def del_med(self,position):
        length=self.len
        if position<0 or position>=length:
            print(f"{position} is invalid")
        elif position==0:
            self.del_beg()
        elif position==length-1:
            self.del_end()
        else:
            q=None
            p=self.head
            for _ in range(position):
                q=p
                p=p.next
            q.next=p.next
            del p
            
            

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

l1.del_med(2)
print("Length of list:{}".format(l1.len))
l1.display()

