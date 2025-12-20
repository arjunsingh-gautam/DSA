# Count number of special character in string
s=input("Enter a string:")
count=0
for x in s:
    if x.isalnum()==False:
        count+=1

print(f"Number of special characters in string '{s}':{count}")
# Time Complexity:O(n)