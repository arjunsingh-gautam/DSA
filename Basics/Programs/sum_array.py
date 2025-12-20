# Program to calculate sum of elements of an array

def sum(array):
    sum_p=0
    for i in array:
        sum_p+=i
    return sum_p

print("Sum of array:[1,3,45,23] is:",sum([1,3,45,23]))