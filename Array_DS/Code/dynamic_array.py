# In this program we will demonstrate how list changes size at run-time
import sys

arr = []
print("value\tarray_size")
for i in range(10):
    arr.append(i)
    print(i, sys.getsizeof(arr),sep='\t')  # watch memory size grow
