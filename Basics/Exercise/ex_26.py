# Armstrong Number:
# Eg. 123= 1^3+2^3+3^3=1+8+27 != 123 : not an armstron number
# Eg. 153= 1^3+5^3 +3^3=1+125+27=153 : yes

def armstrong_num(num):
    length=len(str(num))
    sum=0
    for x in str(num):
        sum+=int(x)**length
    if sum==num:
        return True
    else: 
        return False

print(armstrong_num(153))
print(armstrong_num(123))
