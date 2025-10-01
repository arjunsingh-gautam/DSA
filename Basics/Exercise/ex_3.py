# Write a program to find maximum of two numbers:
class Solution:
    def __init__(self):
        self.l=[int(x) for x in input("Enter two numbers:").split(',')]
        if self.l[0]>self.l[1]:
            max=self.l[0]
            print(f"Max:{max}")
        else:
            max=self.l[1]
            print(f"Max:{max}")

s1=Solution()
print(s1.__dict__)

# time complexit= O(1)