# Write a program to find max of three numbers:

max_num=lambda a,b,c: a if a>b and a>c else b if b>c else c
print(f" Max is:{max_num(5,34,829)}")