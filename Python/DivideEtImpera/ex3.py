"""
3. Se citește de la tastatură un număr natural N. Se consideră o tablă (matrice) pătratică de dimensiuni
2^n * 2^n pe care se scriu numerele naturale de la 1 si 2^n * 2^n prin vizitarea recursivă a celor patru
cadrane ale tablei în ordinea indicată și în figura alăturată: dreapta-sus, stânga-jos,
stânga-sus, dreapta-jos. De exemplu, daca N=2, tabla este completată astfel:
11 9 3 1
10 12 2 4
7 5 15 13
6 8 14 16
Să se afișeze în fișierul tabla.out matricea completată după regulile precizate.
intrare
2
tabla.out
11 9 3 1
10 12 2 4
7 5 15 13
6 8 14 16
"""


def divImp(mat, m, i, j):  # m = lat
	if m == 1:
		global k
		mat[i][j] = k
		k += 1
		return
	divImp(mat, m//2, i, j + m // 2)
	divImp(mat, m//2, i + m // 2, j)
	divImp(mat, m//2, i, j)
	divImp(mat, m//2, i + m // 2, j + m // 2)


def printMat(v):
	print("\n".join([" ".join([f"{x:3}" for x in linie]) for linie in v]))


N = int(input())
# un cadran este 2^(n-1) x 2^(n-1)
M = pow(2, N)
mat = [[0 for _ in range(M)] for _ in range(M)]
k = 1
divImp(mat, M, 0, 0)
printMat(mat)

