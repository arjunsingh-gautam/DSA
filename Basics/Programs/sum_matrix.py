# In this program we calculate the sum of Matrix nxn
def sum_matrix(a,b):
    c=[[0 for _ in range(len(a[0]))] for _ in range(len(a))]
    for i in range(len(a)): # n times
        for j in range(len(a)): # nxn times
            c[i][j]=a[i][j]+b[i][j] #nxn times
    return c
a=[[1,2],[3,4]]
b=[[5,6],[7,8]]
print("Sum of arrays a and b is:",sum_matrix(a,b))

# Time Complexity: t(n)=2n^2 + n ---> O(n**2)
# Space Complexity: a,b,c:n^2 + i,j --> s(n)= 3n**2 + 2 ===> O(n**2)