# generate 10 random numbers from 1 to 20 and append to the list
import random
def randm():
    l=[]
    for i in range(10):
        l.append(int(random.randrange(1,20)))
    return l

print(randm())
