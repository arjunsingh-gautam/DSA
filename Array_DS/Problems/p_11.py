# count number of elements greater than x

l=[9,11,3,23,21,94,38,48,10,37,4,2,1,5]

x=10

l=[x for x in l if x>10]
print(l)
print(len(l))