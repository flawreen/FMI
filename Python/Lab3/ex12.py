"""
7. Se citesc m, n și o matrice cu m linii și n coloane, elementele unei linii fiind date pe o
linie (elementele unei linii date pe o linie separate cu spațiu). Să se construiască în
memorie și să se afișeze matricea transpusă (folosind și comprehensiune).

3 3
1 2 3
4 5 6
7 8 9
1, 0 = 0, 1
2, 0 = 0, 2
2, 1 = 1, 2

"""
def printMatrix(matrix):
    print('\n'.join(''.join([f"{x:3}" for x in linie]) for linie in matrix))

m, n = [int(x) for x in input().split()]
mat = [[int(x) for x in input().split()] for _ in range(m)]
printMatrix(mat)
mat = [[mat[j][i] for j in range(1)] for i in range(m)]
# for i in range(m):
#     for j in range(i):
#         mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

printMatrix(mat)
