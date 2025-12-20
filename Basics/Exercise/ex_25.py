# Find Perfect Number
# Eg. 6--> 1,2,3 = 1+2+3=6 i.e sum of proper divisor is equal to the number

def perfect_num(num):
    l=[1]
    for i in range(2,(num)//2 +1):
        if num%i==0:
            l.append(i)
    if sum(l)==num:
        return True
    else:
        return False

print(perfect_num(6))
print(perfect_num(28))
print(perfect_num(4))