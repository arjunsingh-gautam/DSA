# read string and print characters present at +ve and -ve indexes

s=input("Enter a string:")
index=0
while 0<=index<len(s):
    print(s[index])
    index+=1
index=-1
while -(len(s)+1)<index<0:
    print(s[index])
    index-=1