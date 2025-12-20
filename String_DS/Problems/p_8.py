# Count number of digits present in string
s=input("Enter a string:")
count=0
for x in s:
    if x.isdigit():
        count+=1

print(f"Number of digits in string '{s}':{count}")
# Time Complexity:O(n)