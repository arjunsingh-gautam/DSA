# sort the string (sort the characters present in the given str)

def sort_str(s):
    return ''.join(sorted(s))

print(sort_str("aefgsbxdsor"))

# Time Complexity: O(n*log(n)) # due time taken to sort the string by sorted() function

# Space Complexity: O(n)