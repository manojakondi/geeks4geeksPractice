#Rotate an m by m matrix by 90 degrees.

N = 4

mat = [[0 for x in range(N)] for y in range(N)]

def displayMatrix(mat):
    for i in range(0,N):
        for j in range(0,N):
            print(mat[i][j],end="\t")
        print("\n")

def rotateMatrix(matrix):
    for layer in range(0,int(N/2)):
        first = layer;
        last = N-layer-1;
        for i in range(first,last):
            offset = i-first
            temp = matrix[first][i]
            matrix[first][i] = matrix[last-offset][first]
            matrix[last-offset][first] = matrix[last][last-offset]
            matrix[last][last-offset] = matrix[i][last]
            matrix[i][last] = temp

mat = [ [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16] ]
displayMatrix(mat)
rotateMatrix(mat)
print("Rotated above matrix In-place Counter clockwise",end="\n")
displayMatrix(mat)
