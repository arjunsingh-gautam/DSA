# Strong Number:
# Eg. 123 = 1!+2!+3!=1+2+6!=123 not a strong number
# Eg. 145= 1!+4!+5!=1+24+120=145 strong number

import math
def strong_num(num):
    sum=0
    temp=num
    while temp!=0:
        digit=temp%10
        sum+=math.factorial(digit)
        temp=temp//10
    if sum==num:
        print(sum,num)
        return True
       
    else:
        print(sum,num)
        return False

print(strong_num(145))
print(strong_num(123))
