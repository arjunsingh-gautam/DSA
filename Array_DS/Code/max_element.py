# this code demonstrate the concept of current and best variable which are used during array traversal
# current: state variable which represent current state
# best: state variable which represent best observation observed till current position traversal

arr=[7,182,1029,32,18292]
best=arr[0] # best observation initially
for i in range(1,len(arr)):
    current=arr[i] # store current state of element
    best=max(best,current) # changes best state during traversal

print(f"Maximum number in array is:{best}")