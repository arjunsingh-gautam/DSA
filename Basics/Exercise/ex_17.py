# Reverse a number:
def rev_num(num):
    r=0
    while num!=0:
        d=num%10
        r=r*10+d
        num=num//10
    print(f"Reverse num:{r}")
rev_num(1991)