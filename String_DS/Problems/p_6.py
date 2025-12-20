# Count number of consonants present in the given string
s=input("Enter a string:")
vowels={'a','e','i','o','u'}
count=0
for x in s.lower():
    if x not in vowels:
        count+=1

print(f"Consonants in string {s}:{count}")

# Time Complexity:O(n)