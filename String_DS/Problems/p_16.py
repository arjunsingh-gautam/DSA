#convert even indexed char into upper case and odd indexed char into lower case

s=input("Enter a string:")
result=""
for x in range(len(s)):
    if x%2==0:
        result=result+s[x].upper()
    else:
        result=result+s[x].lower()

print(result)

# Time complexity: O(n^2)

# Optimised Version: Use list since list is mutable it appends the characters and at last we can join each character which O(1) operation:

s=input("Enter a string:")
result=[]
for x in range(len(s)):
    if x%2==0:
        result.append(s[x].upper())
    else:
        result.append(s[x].lower())

print(''.join(result))
# Time Complexity: O(n) since append is O(1) operation