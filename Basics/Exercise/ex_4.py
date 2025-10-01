# Write a program to find minimum of two number:
class Solution:
    def __init__(self):
        self.l=[int(x) for x in input("Enter two number").split(',')]
        print(f"Min:{min(self.l)}")

s1=Solution()

# Time Complexity: O(n) 