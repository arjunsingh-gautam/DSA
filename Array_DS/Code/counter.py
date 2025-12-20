# In this program we will learn about counter a dict subclass which help us to map frequency
from collections import Counter
s="anagram"
c=Counter(s) # to convert an iterable to Counter time complexity: O(n)
print(f"Type of c:{type(c)}\nc is:{c}\n")