# Ex-1: Write a program to read a string and convert all even indexed values into upper case
class Solution:
    def __init__(self):
        self.inp_str=input("Enter a string:")
    def up(self):
        l=[]
        for i in range(0,len(self.inp_str)):
            if i%2==0:
                l.append(self.inp_str[i].upper())
            else:
                l.append(self.inp_str[i].lower())

        print(f"Formatted String:{''.join(l)}")

s1=Solution()
s1.up()


# Time complexit: O(n)