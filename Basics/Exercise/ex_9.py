# min of n values:
def min_value(*args):
    min=args[0]
    for x in args:
        if min>=x:
            min=x
        else:
            pass
    print(f"min is:{min}")

min_value(2929291,3,-924,-8382,6,83)

# Time Complexity:O(n)