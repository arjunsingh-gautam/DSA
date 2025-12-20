# convert odd indexed char into upper case and even indexed char into lower case
s=input("Enter a string:")
result=[]
for x in range(len(s)):
    if x%2==0:
        result.append(s[x].lower())
    else:
        result.append(s[x].upper())

print(''.join(result))
# Time Complexity: O(n) since append is O(1) operation
