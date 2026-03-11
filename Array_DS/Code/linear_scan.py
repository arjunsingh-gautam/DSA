# Implementing Linear scan in Python:
# index based scan
def linear_scan(array):
    for i in range(len(array)):
        print(array[i])
print("Index based scan:")
linear_scan([10,30,40,50,60])

print("Value based scan:")
# value based scan
def value_scan_linear(array):
    for x in array:
        print(x)
value_scan_linear([94,27,19,34])