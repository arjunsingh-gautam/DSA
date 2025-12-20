# Digit extraction 
# Eg. n=123 Digits 1,2,3
def digits(num):
    l=[]
    while num>0:
        l.append(num%10)
        num=num//10
    print(f"Digits list:{l[::-1]}")

num=12234
digits(num)

# Time complexity: O(log(num))


# Alternate solution:
digits=[int(x) for x in str(num)]
print(digits)