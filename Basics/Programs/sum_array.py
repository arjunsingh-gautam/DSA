# Program to calculate sum of elements of an array

def sum(array):
    sum_p=0
    for i in array:
        sum_p+=i
    return sum_p

print("Sum of array:[1,3,45,23] is:",sum([1,3,45,23]))

# Time complexity: t(n):2n+1 --> O(n)
# Space Complexity: sum_p,i,array-->n ---> s(n)=n+2 ---> O(n)