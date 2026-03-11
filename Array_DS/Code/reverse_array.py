# In this we program we will reverse an array: 
# Operations: Swap,Traversal

def rev_array(array):

    for i in range(len(array)//2): # Array Traversal
        array[i],array[len(array)-i-1]=array[len(array)-i-1],array[i] # Swap
    return array

arr=[1,33,23,453,2818]
reversed_array=rev_array(arr)
print(f"Reversed array:{reversed_array}")

# t(n)=O(n)
