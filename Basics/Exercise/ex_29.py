# Tribonacci Number:
# Eg. 0 1 2 3 6 11 ...
def trib(n):
    n1=0
    n2=1
    n3=2
    l=[n1,n2,n3]
    for x in range(3,n):
        new=n1+n2+n3
        l.append(new)
        n1,n2,n3=n2,n3,new
    return l

print(trib(5))
print(trib(13))