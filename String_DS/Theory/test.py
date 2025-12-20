l1=[1,2,3]
l2=l1
print(l1 is l2)
l2.append(4)
print(l1,l2)
print(id(l1),id(l2))
l3=l1.copy()
l3.append(5)
print(l1,l2,l3)
print(id(l1),id(l2),id(l3))