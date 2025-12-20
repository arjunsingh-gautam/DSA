# remove duplicate character from a string

def remove_duplicate(s):
    l=[]
    for x in s:
        if x not in l:
            l.append(x)
    return ''.join(l)
print(remove_duplicate("banana"))
print(remove_duplicate("welcome"))


# Time complexity=O(n)