# Count number of alphabets
s=input("Enter a string:")
count=0
for x in s:
    if x.isalpha():
        count+=1
print(f"Alphabets in string '{s}':{count}")
# Time complexity:O(n)