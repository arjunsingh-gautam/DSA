# sum of digits:
def sum_digits(num):
    sum=0
    while num!=0:
        sum+=(num%10)
        num=num//10
    print(f"Sum of digits of is {sum}")

sum_digits(1828)

# Time Complexity: O(log(num))

