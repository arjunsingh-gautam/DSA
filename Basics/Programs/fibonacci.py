# In this program we will write a program to print n fibonacci sequence and analyse it's time complexity:

# Iterative Solution
import time
start=time.time()
def fibonacci(num):
    t0=0
    t1=1
    print(t0,end=',')
    print(t1,end=',')
    for i in range(num-2):
        tn=t0+t1
        print(tn,end=',')
        t0=t1
        t1=tn


fibonacci(30)
end=time.time()
print("Execution time:", end - start, "seconds")

# Time Complexity: for input n very large the loop runs for n-times therefore the time complexity is O(n)