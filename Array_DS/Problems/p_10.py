# swap first and last element in the list
def swap(l):
    if len(l)==1:
        print("Can't swap")
        return
    temp=l[0]
    l[0]=l[-1]
    l[-1]=temp
    return l

print(swap([1,2,3,4,5]))