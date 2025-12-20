# Sum of even digits in a given number
def even_sum(num):
    sum=0
    while num!=0:
        digit=num%10
        if digit%2==0:
            sum+=digit
        num=num//10
    return sum

print(even_sum(123834))
print(even_sum(39492943))
