# Sum of n natural numbers:
def sum_n(n):
    sum=0
    for i in range(n+1):
        sum+=i
    print(f"Sum of {n} natural number is:{sum}")

sum_n(8)

# Time Complexity: O(n)


def rec_sum(n):
    if n==1:
        return 1
    else:
        return n+rec_sum(n-1)

print(rec_sum(8))

# Time Complexity: O(n)