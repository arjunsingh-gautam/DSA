# Min of 3 numbers:
min_value=lambda a,b,c: a if a<b and a<c else b if b<c else c
print(f"Min is:{min_value(-934,-12,-32)}")