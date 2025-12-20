# sum of elements in list
l=[1,2,38,4.54,454]
print(sum(l))

# Time complexity: O(n)

def sum_l(l):
    sum=0
    for x in l:
        sum+=x
    return sum

print(sum_l(l))
# Time complexity O(n)