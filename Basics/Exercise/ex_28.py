# Fibonacci Number
def fib(n):
    n1=0
    n2=1
    l=[n1,n2]
    for x in range(2,n):
        new=n1+n2
        l.append(new)
        n1,n2=n2,new
    return l

print(fib(5))
print(fib(13))