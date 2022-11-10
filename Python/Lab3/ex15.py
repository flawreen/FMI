"""
10. Se citesc m, n și o matrice cu m linii si n coloane (numerele sunt date câte unul pe linie).
Să se ordoneze crescător elementele de pe prima coloana prin interschimbări de linii și să
se afișeze matricea obținută (fiecare element se va afișa pe 4 caractere).
"""
def printMatrix(matrix):
    print('\n'.join(''.join([f"{x:4}" for x in linie]) for linie in matrix))

m, n = [int(x) for x in input().split()]
mat = [[int(input()) for _ in range(n)] for _ in range(m)]
printMatrix(mat)
for i in range(m):
    for j in range(i+1, n):
        if mat[i][0] > mat[j][0]:
            mat[i], mat[j] = mat[j], mat[i]
printMatrix(mat)
