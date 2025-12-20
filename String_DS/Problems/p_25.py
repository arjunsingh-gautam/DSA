# return middle char(s) from the given string

def mid_char(s):
    if len(s)<=2:
        return s
    return s[1:len(s)-1]

print(mid_char("abc"))

# Time Complexity:O(n)
# Space Complexity:O(n)