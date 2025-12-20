# Factorial of a number

def factorial(n):
    fact=1
    if n<0:
        fact=None
    elif n==0 or n==1:
        fact=1
    elif n>1:
        for i in range(1,n+1):
            fact=fact*i

    return fact

print(factorial(6))

# Time complexity:O(n)

# Recusive solution

def rec_fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*rec_fact(n-1)

print(f"Recursive fact:{rec_fact(7)}")
# Time Complexity: O(n)