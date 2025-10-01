# Wrtie a program to calculate the sum of all elements in a list:

class Solution:
    def __init__(self):
        self.l=[int(x) for x in input("Enter list of numbers").split(',')]
        print(f"List:{self.l}")
        print(f"Sum of list elements:{sum(self.l)}")

s1=Solution()

# Time Complexit:O(n)