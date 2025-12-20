# check whether the string is rotation of another string or not?
def check_rotate(s1,s2):
    if len(s1)!=len(s2):
        return False
    temp=s1*2
    return temp.find(s2) !=-1
print(check_rotate("abcd","dcbc"))