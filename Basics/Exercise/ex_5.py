# Write a program to determine a no. is even or odd
class Solution:
    def __init__(self):
        self.num=int(input("Enter a number:"))
    
    def check_even(self):
        if (self.num%2==0):
            print(f"{self.num} is even")
        else:
            print(f"{self.num} is odd")
    def check_even_2(self):
        if(self.num&1==0):
            print(f"{self.num} is even")
        else:
            print(f"{self.num} is odd")

s1=Solution()
s1.check_even()
s1.check_even_2()