l=["cat","act","hat"]
from collections import Counter
c=Counter(l)
print(c)
for x in l:
    c=Counter(x)
    print(c)