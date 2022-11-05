"""
ex 5
Se citesc m, n și o matrice cu m linii și n coloane, elementele unei linii fiind date pe o
linie (elementele unei linii date pe o linie separate cu spațiu). Se citește în plus un număr
natural k. Să se insereze o linie nouă cu toate elementele 0 intre liniile k și k+1 ale
matricei.
"""
m, n = [int(x) for x in input().split()]
mat = [[int(x) for x in input().split()] for y in range(m)]
k = int(input())
# mat.insert(k, [0 for i in range(n)])  # [0] * n nu e ok ca face copii
# SAU
mat[k+1:k+1] = [[0 for i in range(n)]]
print(mat)
