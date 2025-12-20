# In this program we will demonstrate how list changes size at run-time
import sys

arr = []
for i in range(10):
    arr.append(i)
    print(i, sys.getsizeof(arr))  # watch memory size grow
