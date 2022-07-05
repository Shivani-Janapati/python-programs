x = int(input())
y = int(input())
z = int(input())
n = int(input())
# arr
# for i in range (0,x+1):
#     for j in range (0,y+1):
#         for k in range (0,z+1):
#             if (i+j+k!=n):
#                 print([i,j,k],end=" ")

arr = [[X, Y, Z] for X in range(x+1) for Y in range(y+1) for Z in range(z+1) if X + Y + Z != n]
#Output
print(arr)
