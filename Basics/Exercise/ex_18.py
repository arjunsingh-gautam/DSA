# Palindrom number check
def palindrome(num):
    if num==int(str(num)[::-1]):
        print(f"{num} is palindrome")

palindrome(19191)