# check wheter string is palindrome
def ispalindrome(s):
    w=1
    for i in range(len(s)):
        if s[i]==s[len(s)-w]:
            w+=1
        else:
            return False
    else:
        return True

print(ispalindrome("mamam"))
print(ispalindrome("man"))

# Time Complexity: O(n)