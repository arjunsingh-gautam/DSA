# get smaller elements from a list less then the given element x

l=[9,11,15,12,3,7,14,10]
print(len(l))
x=10

l = [val for val in l if val <x]

print(f"Updated List: {l}")