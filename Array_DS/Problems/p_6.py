# Average of elements present in the list:

l=[1,2,4.34,82,28]
def avg(l):
    sum=0
    for x in l:
        sum+=x
    return sum/len(l)

print(avg(l))
# Time Complexity:O(n)