# In this code we will solve fibonacci sequence using naive alogrithm
import time
start = time.time()
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

n = 30
for i in range(n):
    print(fib(i), end=" ")

end=time.time()
print("Execution time:", end - start, "seconds")