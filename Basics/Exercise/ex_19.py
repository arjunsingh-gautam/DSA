# Trailing zeros of factorial
import math
def trai_o(num):
    fact=math.factorial(num)
    t=fact
    count=0
    while t!=0:
        if t%10!=0:
            break
        count+=1
        t=t//10
    print(f"Number of trailing zeros in {fact}:{count}")

trai_o(21)