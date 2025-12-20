# generate a list with even and odd elements in the range of 0 to 10
even=[]
odd=[]
for x in range(11):
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)

print(even)
print(odd)

# Time complexity: O(n)