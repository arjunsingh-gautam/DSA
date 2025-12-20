# read and write elements in list
l=[eval(x) for x in input("Enter the list elements:").split(',')]
print(l)
for x in l:
    print(x,type(x))