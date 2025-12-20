# In this program we calculate the sum of Matrix nxn
def sum_matrix(a,b):
    c=[[0 for _ in range(len(a[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a)):
            c[i][j]=a[i][j]+b[i][j]
    return c
a=[[1,2],[3,4]]
b=[[5,6],[7,8]]
print("Sum of arrays a and b is:",sum_matrix(a,b))