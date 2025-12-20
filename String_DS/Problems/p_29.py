# Remove vowels from a string
vowels="aeiouAEIOU"
def remove_vowels(s):
    output=[]
    for x in s:
        if x not in vowels:
            output.append(x)
    return ''.join(output)

print(remove_vowels("Welcome"))

# Time complexity: O(n)
