# All divisors of N:
def div(num):
    l=[1,num]
    for i in range(2,(num)//2 +1):
        if num%i==0:
            l.append(i)
    return l

print(div(493))
print(div(843))
print(div(1024))
print(div(29))