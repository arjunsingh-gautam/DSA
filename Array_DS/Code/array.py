# implementing array using class and list

class MyArray:
    def __init__(self,capacity=10):
        self.capacity=capacity
        self.size=0
        self.data=[None]*capacity # safe initialisation

    def __len__(self): # Help to implement len() method in custom class and change it's behavior
        return self.size
    
    def is_full(self): # check whether the array is empty or full
        if self.size==self.capacity:
            return True

    def get(self,index): # Getter method fetch value at index
        if 0<=index<self.size:
            return self.data[index]
        raise IndexError("Index out of bounds")

    def set(self,index,value): # setter method helps to set value at the index
        if 0<=index<self.size:
            self.data[index]=value
        else:
            raise IndexError("Index out of bounds")

    def append(self,value):
        if self.is_full():
            self._resize(2*self.capacity)
        self.data[self.size]=value
        self.size+=1

    def insert(self,index,value):
        if not(0<=index<=self.size):
            raise IndexError("Index out of bound")
        if self.is_full():
            self._resize(2*self.capacity)
        for i in range(self.size,index,-1):
            self.data[i]=self.data[i-1]
        self.data[index]=value
        self.size+=1

    def pop(self,index=None):
        if self.size==0:
            raise IndexError("pop from empty array")
        if index is None:
            index=self.size-1
        if not(0<=index<self.size):
            raise IndexError("Index out of bounds")
        val=self.data[index]
        for i in range(index,self.size-1):
            self.data[i]=self.data[i+1]
        self.data[self.size-1]=None
        self.size-=1

    def traverse(self):
        return [self.data[i] for i in range(self.size)]

    def _resize(self,new_capacity):
        new_data=[None]*new_capacity
        for i in range(self.size):
            new_data[i]=self.data[i]
        self.data=new_data
        self.capacity=new_capacity


arr=MyArray(5)
arr.append(10)
arr.append(20)
arr.append(30)
print(len(arr))
print(arr.traverse())
arr.set(2,45)
print(arr.traverse())
print(arr.get(1))
arr.insert(1,83)
print(arr.traverse())
arr.pop()
print(arr.traverse())
print(arr.__dict__)