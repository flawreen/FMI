"""
6. Se citesc m, n și o matrice cu m linii și n coloane, elementele unei linii fiind date pe o
linie (elementele unei linii date pe o linie separate cu spațiu). Se citește în plus un număr
natural k. Să se permute fiecare linie a matricei circular la dreapta cu k poziții
(Echivalent: Să se permute coloanele matricei circular spre dreapta cu k poziții)
1 2 3
k = 2
v[2] = -3 + (2+2) % n = -3 +1 = 1
v[1] = -n + (i + k) % n = -3 - (1 + 2) % 3 = 0
v[0] = -3 + (0 + 2) % 3 = -3 + 2 = 2
x = v[(0+2)%3]
1 2 3; 3 = v[-2] ; 2 = v[-3]; 1 v[-3] v[-2]

k = 1
 0  1  2
-3 -2 -1
v[2] = (2 + 1) % 3 = 0
v[1] = (1 + 1) % 3 = 2
v[0] = (0 + 1) % 3 = x
x = v[(0+1)%3]

"""
def printMatrix(matrix):
    print('\n'.join([''.join([f"{x:3}" for x in y]) for y in matrix]))

m, n = [int(x) for x in input().split()]
mat = [[int(x) for x in input().split()] for _ in range(m)]
k = int(input()) % n
# printMatrix(mat)
for linie in mat:
    for _ in range(k):
        x = [linie[-1]]
        for i in range(n-1, 0, -1):
            linie[i:i+1] = [linie[i-1]]
        linie[0:1] = x
printMatrix(mat)
