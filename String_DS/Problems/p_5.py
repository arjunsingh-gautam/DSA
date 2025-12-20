# count number of vowels present in the given string
s=input("Enter a string:")
vowels={'a','e','i','o','u'}
count=0
for x in s.lower():
    if x in vowels:
        count+=1

print(f"No. of vowels in {s} is {count}")
# Time complexity: O(n)