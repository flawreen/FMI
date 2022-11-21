"""
12. Se citește un număr natural N.
a) Să se genereze și afișeze o matrice de dimensiune NxN, cu elementele de la 1 la N*N -
în ordine crescătoare, de la stânga la dreapta și de sus în jos (folosind și comprehensiune).

b) Pentru a parcurge elementele matricei în spirală, pornind din colțul din stânga-sus (spre
dreapta, în jos, spre stânga, în sus, ...), să se obțină întâi o listă având elemente de tip
tuplu (linie, coloană) care să reprezinte pozițiile care trebuie parcurse în această spirală.

c) Folosind lista de tupluri de mai sus, să se afișeze elementele din matrice aflate la acele
poziții.
lista_poz = [(0, 0), (0, 1), ..., (0, N-2), (0, N-1), (1, N-1), ..., (N-2, N-1), (N-1, N-1), (N-1, N-2), ..., (N-1, 1), (N-1, 0), (N-2, 0), ..., (1, 0), (1,1), (1, 2), ...]
spirala = [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]
"""
def printMatrix(matrix):
    print('\n'.join(''.join([f"{x:4}" for x in linie]) for linie in matrix))

def genTuples(n, k, ls):
    if n < k:
        return

    ls.extend([(k, i) for i in range(k, n-1)])
    ls.extend([(i, n-1) for i in range(k, n-1)])
    ls.extend([(n-1, i) for i in range(n-1, k, -1)])
    ls.extend([(i, k) for i in range(n-1, k, -1)])

    genTuples(n-1, k+1, ls)


nr = int(input())
# a)
mat = [[i*nr + j+1 for j in range(nr)] for i in range(nr)]
printMatrix(mat)

# b)
indexx = []
genTuples(nr, 0, indexx)
if nr & 1:
    indexx.append((nr//2, nr//2))
# c)
spirala = [mat[x[0]][x[1]] for x in indexx]
print(spirala)
