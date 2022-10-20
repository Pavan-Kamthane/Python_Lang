# Python3 Program to find
# transpose of a matrix

M = 3
N = 4

# This function stores
# transpose of A[][] in B[][]

def transpose(A, B):

for i in range(N):
for j in range(M):
B[i][j] = A[j][i]

# driver code
A = [ [1, 1, 1, 1],
[2, 2, 2, 2],
[3, 3, 3, 3]]


# To store result
B = [[0 for x in range(M)] for y in range(N)]

transpose(A, B)

print("Result matrix is")
for i in range(N):
for j in range(M):
print(B[i][j], " ", end='')
print()
