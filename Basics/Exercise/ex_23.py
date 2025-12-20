# sum of prime digits:
def isprime(num):
    if num==1 or num==0:
            return False
    for i in range(2,(num//2)+1):
        if num%i==0:
            return False
    return True

def prime_sum(num):
    sum=0
    while num!=0:
        digit=num%10
        if isprime(digit):
            sum+=digit
        num=num//10
    return sum

print(prime_sum(129382))
print(prime_sum(8439297))
