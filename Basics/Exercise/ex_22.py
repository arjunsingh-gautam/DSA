# sum of odd digits in the given number:
def odd_sum(num):
    sum=0
    while num!=0:
        digit=num%10
        if digit%2!=0:
            sum+=digit
        num=num//10
    return sum

print(odd_sum(123834))
print(odd_sum(39492943))