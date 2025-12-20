# Swapping two numbers:
def swap1(a,b):
    print(f"Before swap:a={a} and b={b}")
    t=a
    a=b
    b=t
    print(f"After swap:a={a} and b={b}")
def swap2(a,b):
    print(f"Before swap:a={a} and b={b}")
    a,b=b,a
    print(f"After swap:a={a} and b={b}")
def swap3(a,b):
    print(f"Before swap:a={a} and b={b}")
    a=a+b
    b=a-b
    a=a-b
    print(f"After swap:a={a} and b={b}")
def swap4(a,b):
    print(f"Before swap:a={a} and b={b}")
    a=a*b
    b=a//b
    a=a//b
    print(f"After swap:a={a} and b={b}")
def swap5(a,b):
    print(f"Before swap:a={a} and b={b}")
    a=a^b
    b=a^b
    a=a^b
    print(f"After swap:a={a} and b={b}")





swap1(5,6)
swap2(4,6)
swap3(5,4)
swap4(-3,6)
swap5(5,-6)