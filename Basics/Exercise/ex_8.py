# max of n numbers:
def max_value(*args):
    max=args[0]
    for x in args:
        if max<=x:
            max=x
        else:
            pass
    print(f"Max is:{max}")

max_value(2929291,3,4,8382,6,83)

# Time Complexity:O(n)